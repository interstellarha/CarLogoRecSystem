import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Recognizing import Ui_Recognizing
from Recognizing2 import Ui_Recognizing2
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
#from predict import result
from PIL import Image
import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec

# Importing keras and its deep learning tools - neural network model, layers, contraints, optimizers, callbacks and utilities
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.constraints import maxnorm
from keras.optimizers import adam, RMSprop, SGD
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.utils import np_utils
from keras.regularizers import l2
from keras.initializers import RandomNormal, VarianceScaling
# Importing scikit-learn tools
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
# Setting up the image pool
import sqlite3 #执行sqlite3数据库操作
from Ui_LeftSingleBlock import Ui_LeftSingleBlock #组合部件：左侧每辆推荐的车的模板
import CarRecommendSpider  # 爬取当前品牌推荐车辆信息
import requests

OpenFilePath = " "
result = " "
class SelectWin(QWidget, Ui_Recognizing):
    def __init__(self):
        super(SelectWin,self).__init__()
        self.setupUi(self)

    def openImage(self):
        imgName,imgType = QFileDialog.getOpenFileName(self,"select","img","*.jpg;*.tif;*.png;;All Files(*)")
        if imgName == "":
            return 0
        jpg = QPixmap(imgName).scaled(self.label.width(),self.label.height())
        self.label.setPixmap(jpg)

        #图片路径
        global OpenFilePath
        OpenFileInfo = QFileInfo(imgName)
        OpenFilePath = OpenFileInfo.filePath()
        print(OpenFilePath)

    def Recognizing(self):
        new_image_path = OpenFilePath
        # new_imgs = os.listdir(new_image_path)
        # new_n_samples = np.size(new_imgs)
        im = Image.open(new_image_path).convert("RGB")
        new_im = np.array(im.resize((50, 50))).flatten()
        m = int(model.predict_classes(ImageConvert(1, new_im), verbose=0))
        global result
        result = cars[m]
        print(result)
        # 关闭当前窗口打开新窗口
        self.hide()
        self.newWindow = ResultWin()
        self.newWindow.show()
        return result

class ResultWin(QWidget,Ui_Recognizing2):
    def __init__(self):
        super(ResultWin,self).__init__()
        self.setupUi(self)
        global OpenFilePath,result
        img = QPixmap(OpenFilePath).scaled(self.pic.width(),self.pic.height())
        self.conn = sqlite3.connect("database.db")
        print("connect database successfully")
        self.cur = self.conn.cursor()
        self.pic.setPixmap(img)
        self.name.setText(result)
        self.iLike.clicked.connect(self.ILike)
        self.briefIntro.setText(str(self.ShowInfo()))
        self.back.clicked.connect(self.BackToSelect)
        # 左侧：推荐信息
        #######################################################
        self.reCommendList = CarRecommendSpider.main(str(result))  # 12辆车
        print(self.reCommendList)
        carNum = len(self.reCommendList)  # 推荐车的数量
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10,40,400,115*carNum))
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(10,40,400,115*carNum))
        self.addRecommendCars()

    def ShowInfo(self):
        # 数据库操作
        self.cur.execute("SELECT * FROM CAR_BRAND WHERE cname = \"{carname}\"".format(carname=result))
        info = self.cur.fetchone()
        print(info[3])
        return info[3]

    def ILike(self):
        #创建品牌——用户表
        sql = '''
             CREATE TABLE IF NOT EXISTS ILIKE
             (
             brand varchar,
             userName varchar
             )
        '''
        print("create successfully")
        self.cur.execute(sql)
        self.conn.commit()
        #添加喜欢信息，并判断是否曾经存在过
        sql2 = '''
              INSERT INTO ILIKE 
              (brand,userName) values(\"{brand}\",\"{userName}\")
        '''.format(brand = result,userName = "noname")
        sql3 = '''
             SELECT * FROM ILIKE WHERE userName = \"{userName}\" 
        '''.format(userName = "noname")
        self.cur.execute(sql3)
        info = self.cur.fetchone()
        if info != None and str(info[0])==result:
            print("Already exists")
            self.likeShow.setText("Already liked!")
            return
        else:
            self.likeShow.setText("Like it!")
            self.cur.execute(sql2)
            self.conn.commit()
            print("successfully insert")
            return

    def BackToSelect(self):
        self.hide()
        m.show()
        return

    def addRecommendCars(self):
        for item in self.reCommendList: #循环每个推荐车辆
            self.car = Ui_LeftSingleBlock(item)
            self.verticalLayout.addWidget(self.car)
            self.verticalLayout.addStretch(1)
        return

cars = ['Alfa Romeo', 'Audi', 'BMW', 'Chevrolet', 'Citroen', 'Dacia', 'Daewoo', 'Dodge',
        'Ferrari', 'Fiat', 'Ford', 'Honda', 'Hyundai', 'Jaguar', 'Jeep', 'Kia', 'Lada',
        'Lancia', 'Land Rover', 'Lexus', 'Maserati', 'Mazda', 'Mercedes', 'Mitsubishi',
        'Nissan', 'Opel', 'Peugeot', 'Porsche', 'Renault', 'Rover', 'Saab', 'Seat',
        'Skoda', 'Subaru', 'Suzuki', 'Tata', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo']

kwrds = ['logo', 'logotype', 'logo png', 'logo gif', 'logo jpg', 'logo front',
         'logo rear', 'badge', 'logo white', 'logo black', 'logo transparent']

img_x = img_y = 50 # image size is constant
n_channels = 3

model = Sequential()
model.add(Conv2D(32, (3,3),
                 input_shape=(img_x,img_y,n_channels),
                 padding='valid',
                 bias_initializer='glorot_uniform',
                 kernel_regularizer=l2(0.00004),
                 kernel_initializer=VarianceScaling(scale=2.0, mode='fan_in', distribution='normal', seed=None),
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64, (3,3),
                 padding='valid',
                 bias_initializer='glorot_uniform',
                 kernel_regularizer=l2(0.00004),
                 kernel_initializer=VarianceScaling(scale=2.0, mode='fan_in', distribution='normal', seed=None),
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(128, (3,3),
                 padding='valid',
                 bias_initializer='glorot_uniform',
                 kernel_regularizer=l2(0.00004),
                 kernel_initializer=VarianceScaling(scale=2.0, mode='fan_in', distribution='normal', seed=None),
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(256, (3,3),
                 padding='valid',
                 bias_initializer='glorot_uniform',
                 kernel_regularizer=l2(0.00004),
                 kernel_initializer=VarianceScaling(scale=2.0, mode='fan_in', distribution='normal', seed=None),
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(4096, activation='relu', bias_initializer='glorot_uniform'))
model.add(Dropout(0.5))

model.add(Dense(4096, activation='relu', bias_initializer='glorot_uniform'))
model.add(Dropout(0.5))

# final activation is softmax, tuned to the number of classes/labels possible
model.add(Dense(len(cars), activation='softmax'))

model.load_weights('car_CNN_13AUGM_CMCMCMCMF.h5py')

def ImageConvert(n, i):
    im_ex = i.reshape(n, img_x, img_y, 3)
    im_ex = im_ex.astype('float32') / 255
    im_ex = np.subtract(im_ex, 0.5)
    im_ex = np.multiply(im_ex, 2.0)
    return im_ex


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    m = SelectWin()
    m.select.clicked.connect(m.openImage)
    #print(OpenFilePath)
    m.recognize.clicked.connect(m.Recognizing)
    m.show()
    '''
    MainWindow = QMainWindow()
    ui = Ui_Recognizing()
    ui.setupUi(MainWindow)
    MainWindow.show()
    '''
    sys.exit(app.exec_())
