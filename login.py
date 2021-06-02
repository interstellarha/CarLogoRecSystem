# -*- coding: utf-8 -*-
# @Time: 2021/5/14 21:20
# @Author: 车诗琪+其他文件整合
# @File: login
# @Project: HWprogram
import sys
import os
import sqlite3  # 用于数据库
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QAction, QLineEdit, QMainWindow
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QIcon
from login_ui import Ui_login
from register import FormSignUp
#from index import FormIndex
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
from keras.optimizers import Adam, RMSprop, SGD
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.utils import np_utils
from keras.regularizers import l2
from keras.initializers import RandomNormal, VarianceScaling
# Importing scikit-learn tools
# from sklearn.utils import shuffle
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix
# Setting up the image pool
import sqlite3 #执行sqlite3数据库操作
from Ui_LeftSingleBlock import Ui_LeftSingleBlock #组合部件：左侧每辆推荐的车的模板
import CarRecommendSpider  # 爬取当前品牌推荐车辆信息
import requests
from index_ui import Ui_index
import globalvar as gl
from search import Ui_MainWindow
from CarRecommendSpider import *
from _infoPage import personalInfoPage
# import LefBlockImg_src

gl._init()  # 初始化全局变量管理模块
gl.set_value('username', "")  # 设置变量值 username

OpenFilePath = " "
result = " "
username = " "
def common(cn, sql):
    """将数据从sql格式转换成列表镶嵌字典的格式并返回"""
    cursor = cn.execute(sql)
    information = []
    for row in cursor:
        information.append(row)
    return information


def judge_account(account):
    """用于判断账号是否存在"""
    cn = sqlite3.connect("database.db")
    sql = '''SELECT DISTINCT name
             FROM user
          '''
    aaccounts = common(cn, sql)
    for acc in aaccounts:
        if acc[0] == account:
            return 1  # 返回1说明账号存在
    return 0


def judge_ac_and_pw( account, password):
    """用于判断账号和密码是否匹配"""
    cn = sqlite3.connect("database.db")
    cursor = cn.cursor()
    sql = '''SELECT DISTINCT name, pwd
             FROM user WHERE name=?
          '''
    result = cursor.execute(sql, (account,))
    data = result.fetchall()
    if account and password:  # 如果两个都不空
        if data:
            if str(data[0][1]) == password:
                return 1
            else:
                return 0


class FormSignIn(QMainWindow, Ui_login):
    def __init__(self, parent=None):
        super(FormSignIn, self).__init__(parent)
        self.setupUi(self)

        ## 绑定按钮事件
        self.logIn.clicked.connect(self.on_button_login)
        self.cancel.clicked.connect(self.on_button_cancel)

    def on_button_cancel(self):
        self.close()

    def on_button_login(self):  # 按下“登录”的按钮
        account = self.lineEdit_account.text()

        count = judge_account(account)
        if count != 1:
            reply = QMessageBox.warning(self, "警告", "账号不存在，请重新输入", QMessageBox.Retry, QMessageBox.Retry)
            if reply == QMessageBox.Retry:
                self.lineEdit_account.clear()
                self.lineEdit_password.clear()
        else:
            password = self.lineEdit_password.text()
            count = judge_ac_and_pw(account, password)
            if count == 1:
                reply = QMessageBox.information(self, '恭喜', '登录成功!', QMessageBox.Ok, QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    self.hide()
                    self.mywindow = FormIndex()
                    gl.set_value('username', account)  # 设置变量值 user
                    self.mywindow.account = account
                    self.mywindow.show()
            else:
                reply = QMessageBox.warning(self, "警告", "密码错误", QMessageBox.Retry, QMessageBox.Retry)
                if reply == QMessageBox.Retry:
                    self.lineEdit_password.clear()

class SelectWin(QWidget, Ui_Recognizing):
    def __init__(self):
        super(SelectWin,self).__init__()
        self.setupUi(self)
        self.select.clicked.connect(self.openImage)
        self.recognize.clicked.connect(self.Recognizing)
        self.return_2.clicked.connect(self.ReturnToIndex)
        self.timer = QTimer()
        self.timer.timeout.connect(self.ShowTime)#通过调用槽函数刷新时间
        self.timer.start(1000)

    def ShowTime(self):
        #self.timer.start(1000) #1000ms刷新一次
        time = QTime.currentTime()#获取当前时间
        date = QDate.currentDate()
        timedisplay = time.toString("hh:mm:ss") #格式化时间
        datedisplay = date.toString("yyyy-MM-dd") #格式化日期
        self.time.setText(timedisplay)
        self.date.setText(datedisplay)

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
        self.newwindow = ResultWin()
        self.newwindow.show()
        return result

    def ReturnToIndex(self):
        self.hide()
        dialog.show()

class ResultWin(QWidget,Ui_Recognizing2):
    def __init__(self):
        super(ResultWin,self).__init__()
        # win = QMainWindow()
        # win.setObjectName('window1')
        # win.setStyleSheet("#Recognizing2{border-image:url(./pyqtpic/recommend.jpg);}")
        self.setupUi(self)
        global OpenFilePath,result
        img = QPixmap(OpenFilePath).scaled(self.pic.width(),self.pic.height())
        self.conn = sqlite3.connect("database.db")
        print("connect database successfully")
        self.cur = self.conn.cursor()
        self.pic.setPixmap(img)
        self.name.setText(result)
        self.iLike.clicked.connect(self.ILike)
        self.textBrowser.setText(str(self.ShowInfo()))
        self.back.clicked.connect(self.BackToSelect)
        # 左侧：推荐信息
        #######################################################
        self.reCommendList = CarRecommendSpider.get_one_brand(str(result))  # 12辆车
        #print(self.reCommendList)

        carNum = len(self.reCommendList)  # 推荐车的数量

        if(len(self.reCommendList)==0):
            print("no recommendation")
            self.scrollArea_2.hide()
            # self.label = QLabel("暂无推荐信息")
            # self.label.setAlignment(Qt.AlignRight)
            # self.label.setStyleSheet("color:rgb(20,20,20,255);font-size:16px;font-weight:bold:text")
        else:
            self.message.hide()
            self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 500, 104.5 * carNum))
            # self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(10, 40, 500, 115 * carNum))
            # self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(500, 115 * carNum))
            self.addRecommendCars()

        self.ShowDataPic()
        self.getPersonalInfo()

    def ShowInfo(self):
        # 数据库操作
        # print(str(result))
        self.cur.execute("SELECT * FROM CAR_BRAND WHERE cname = \"{carname}\"".format(carname=str(result)))
        info = self.cur.fetchone()
        # print(info[3])
        return info[3]

    def ILike(self):
        global username
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
        #
        #添加喜欢信息，并判断是否曾经存在过
        sql2 = '''
              INSERT INTO ILIKE 
              (brand,userName) values(\"{brand}\",\"{userName}\")
        '''.format(brand = result,userName = username)
        sql3 = '''
             SELECT * FROM ILIKE WHERE userName = \"{userName}\" 
        '''.format(userName = username)
        self.cur.execute(sql3)
        info = self.cur.fetchall()
        #print(info[0])
        if info != None:
            i = len(info)
            j = 0
            while j <= (i - 1):
                if info[j][0] == result:
                    print("Already exists")
                    self.likeShow.setText("Already liked!")
                    self.conn.commit()
                    return
                j += 1
            self.likeShow.setText("Like it!")
            self.cur.execute(sql2)
            self.conn.commit()
            print("successfully insert")
            return
        else:
            self.likeShow.setText("Like it!")
            self.cur.execute(sql2)
            self.conn.commit()
            print("successfully insert")
            return

    def BackToSelect(self):
        self.hide()
        SelectWindow.show()
        return
    
    #查询结果：左侧循环出现每辆车
    def addRecommendCars(self):
        for item in self.reCommendList: #循环每个推荐车辆
            self.car = Ui_LeftSingleBlock(item)
            self.verticalLayout.addWidget(self.car)
            self.verticalLayout.addStretch(1)

    def ShowDataPic(self):
        sql = '''
                    SELECT * from CAR_BRAND where cname = \"{ename}\"
                '''.format(ename=result)  # 从数据库查询检测到的品牌
        print("查询品牌信息...")
        self.cur.execute(sql)
        self.brandInfo = self.cur.fetchone()  # 一行
        print("查询成功...")  # 得到tuple
        url = self.brandInfo[2]
        req = requests.get(url)
        logo = QtGui.QPixmap()
        logo.loadFromData(req.content)
        logo = logo.scaled(QtCore.QSize(self.origin.width(),self.origin.height()))
        self.origin.setPixmap(logo)

    def getPersonalInfo(self):
        """得到当前登录用户的用户名"""
        global username
        username = gl.get_value('username')
        '''
        """在数据库中，查找登录用户的信息"""
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('database.db')
        db.open()

        query = QSqlQuery()
        sql = "SELECT * FROM user WHERE name='%s'" % username
        query.exec_(sql)

        if not query.exec_():
            query.lastError()
        else:
            while query.next():
                passwd = query.value(2)
                registerTime = query.value(3)
                gl.set_value('passwd', passwd)
                gl.set_value('registerTime', registerTime)
        '''

cars = ['AlfaRomeo', 'Audi', 'BMW', 'Chevrolet', 'Citroen', 'Dacia', 'Daewoo', 'Dodge',
        'Ferrari', 'Fiat', 'Ford', 'Honda', 'Hyundai', 'Jaguar', 'Jeep', 'Kia', 'Lada',
        'Lancia', 'LandRover', 'Lexus', 'Maserati', 'Mazda', 'Mercedes', 'Mitsubishi',
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

class FormIndex(QWidget, Ui_index):
    def __init__(self, parent=None):
        super(FormIndex, self).__init__(parent)
        self.setupUi(self)
        self.logoRecognition.clicked.connect(self.EnterRecog)
        self.carLogo.clicked.connect(self.carLogoClicked)
        self.home.clicked.connect(self.EnterHome)

    def EnterRecog(self):
        self.hide()
        SelectWindow.show()

    def carLogoClicked(self):
        self.hide()
        self.MainWindow = QMainWindow()
        self.test = Ui_MainWindow()
        self.test.setupUi(self.MainWindow)
        self.test.backToHome.clicked.connect(self.comeBack)
        self.MainWindow.show()
    
    def comeBack(self):
        self.MainWindow.hide()
        self.show()

    def EnterHome(self):
        self.Home = personalInfoPage()
        self.Home.show()

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    signin = FormSignIn()
    signup = FormSignUp()
    SelectWindow = SelectWin()
    dialog = FormIndex()
    #dialog.show()
    signin.show()
    signin.register_2.clicked.connect(signup.show)
    sys.exit(app.exec_())
