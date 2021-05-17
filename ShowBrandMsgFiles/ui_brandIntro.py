# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brandIntro.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog,QMessageBox,QAction
import sys
import sqlite3
import requests


class Ui_BrandIntro(object):
    def __init__(self,brandEname): #传入品牌英文名（识别结果）
        print("连接数据库...")
        self.conn = sqlite3.connect("database.db") #连接数据库
        print("连接成功...")
        self.cursor = self.conn.cursor()
        
        #从数据库查询检测到的品牌
        sql = '''
            SELECT * from CAR_BRAND where cname = \"{ename}\"
        '''.format(ename = brandEname)
        print("查询品牌信息...")
        self.cursor.execute(sql)
        self.brandInfo = self.cursor.fetchone() #一行
        print("查询成功...") #得到tuple


    def setupUi(self, Form): 
        Form.setObjectName("Form")
        Form.resize(981, 646)


        self.carLogo = QtWidgets.QLabel(Form)
        self.carLogo.setGeometry(QtCore.QRect(512, 93, 111, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carLogo.sizePolicy().hasHeightForWidth())
        self.carLogo.setSizePolicy(sizePolicy)
        self.carLogo.setObjectName("carLogo")
        

        self.enameTitle = QtWidgets.QLabel(Form)
        self.enameTitle.setGeometry(QtCore.QRect(630, 120, 72, 18))
        self.enameTitle.setObjectName("enameTitle")

        self.cnameTitle = QtWidgets.QLabel(Form)
        self.cnameTitle.setGeometry(QtCore.QRect(630, 147, 72, 18))
        self.cnameTitle.setObjectName("cnameTitle")

        self.introText = QtWidgets.QTextBrowser(Form)
        self.introText.setGeometry(QtCore.QRect(511, 248, 331, 300))
        self.introText.setObjectName("introText")

        self.introTitle = QtWidgets.QLabel(Form)
        self.introTitle.setGeometry(QtCore.QRect(510, 220, 72, 18))
        self.introTitle.setObjectName("introTitle")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(700, 550, 144, 18))
        self.label.setObjectName("label")

        self.ename = QtWidgets.QLabel(Form)
        self.ename.setGeometry(QtCore.QRect(710, 120, 81, 18))
        self.ename.setObjectName("ename")

        self.cname = QtWidgets.QLabel(Form)
        self.cname.setGeometry(QtCore.QRect(710, 147, 81, 18))
        self.cname.setObjectName("cname")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.enameTitle.setText(_translate("Form", "英文名："))
        self.enameTitle.adjustSize()
        self.cnameTitle.setText(_translate("Form", "中文名："))
        self.introTitle.setText(_translate("Form", "品牌介绍"))

        #print(self.brandInfo)
        self.ename.setText(_translate("Form", self.brandInfo[0])) #中文名
        self.ename.resize(len(self.brandInfo[0])*10,18)

        self.cname.setText(_translate("Form", self.brandInfo[1])) #英文名
        #self.cname.resize(len(self.brandInfo[1])*20,18)

        self.introText.setText(_translate("Form", self.brandInfo[3])) #介绍

        self.label.setText(_translate("Form", '更详细内容请<a href="%s">点击</a>'%self.brandInfo[4]))
        self.label.setOpenExternalLinks(True)  # 使成为超链接，外部浏览器打开

        url = self.brandInfo[2]
        req = requests.get(url)
        logo = QtGui.QPixmap()
        logo.loadFromData(req.content)
        logo = logo.scaled(QtCore.QSize(80, 80))
        self.carLogo.setPixmap(logo)


         
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()

    #showBrandIntro = Ui_BrandIntro(result) #传入识别结果，一下均为测试

    #可能是字符编码问题，下行可以，下下行不行
    #showBrandIntro = Ui_BrandIntro("Land Rover") #不行
    #showBrandIntro = Ui_BrandIntro("Land Rover") #可以
    showBrandIntro = Ui_BrandIntro("Audi") #可以

    showBrandIntro.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())