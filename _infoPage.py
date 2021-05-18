# -*- coding: utf-8 -*-
# @Time: 2021/5/16 21:50
# @Author: 车诗琪
# @File: infoPage

import sys
import os
import sqlite3  # 用于数据库
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtSql import *
from PIL import Image

import globalvar as gl
from _infoPage_ui import Ui_Info
from _modifyPassword import modifyPasswordPage

gl._init()  # 初始化全局变量管理模块
OpenFilePath = " "


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def updateBLOB(icon, username):
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        sqlite_update_blob_query = """ UPDATE user SET portrait = ? WHERE name = ? """

        binaryIcon = convertToBinaryData(icon)
        # 在数据库中，更新登录用户的portrait
        cursor.execute(sqlite_update_blob_query, (binaryIcon, username))
        sqliteConnection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()


def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    # print("Stored blob data into: ", filename, "\n")


def readBlobData(username):
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()

        sql_fetch_blob_query = """SELECT * from user where name = ?"""
        cursor.execute(sql_fetch_blob_query, (username,))
        record = cursor.fetchall()
        for row in record:
            name = row[1]
            photo = row[4]

            # print("Storing portrait image on disk \n")
            photoPath = "./sqlite_create/" + username + ".jpg"
            writeTofile(photo, photoPath)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()


class personalInfoPage(QMainWindow, Ui_Info):
    def __init__(self, parent=None):
        super(personalInfoPage, self).__init__(parent)
        self.getPersonalInfo()
        self.setupUi(self)

        # 绑定按钮事件
        self.changePortrait.clicked.connect(self.clickChangePortrait)
        # self.favoriteBrand.clicked.connect(self.clickFavoriteBrand)
        self.modifyPassword.clicked.connect(self.clickModifyPassword)

    def getPersonalInfo(self):
        """得到当前登录用户的用户名"""
        username = gl.get_value('username')

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

        # 从数据库中读出二进制图片，存入"D:\sqlite_create\username.jpg"
        readBlobData(username)

        #保存头像图片路径
        # imgPath = ".\\sqlite_create\\" + username + ".jpg"
        # gl.set_value('imgPath', imgPath)

        # jpg = QPixmap(imgPath).scaled(self.label_icon.width(), self.label_icon.height())
        # self.label_icon.setPixmap(jpg)

    #点击 “更改头像” 按钮
    def clickChangePortrait(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "select", "img", "*.jpg;*.tif;*.png;;All Files(*)")
        if imgName == "":
            return 0
        jpg = QPixmap(imgName).scaled(self.label_icon.width(), self.label_icon.height())
        self.label_icon.setPixmap(jpg)

        #图片路径
        global OpenFilePath
        OpenFileInfo = QFileInfo(imgName)
        OpenFilePath = OpenFileInfo.filePath()

        """得到当前登录用户的用户名"""
        username = gl.get_value('username')

        #将图片转化为二进制数据，更新数据库
        updateBLOB(imgName, username)

    # 点击 “我喜欢的品牌” 按钮
    # def clickFavoriteBrand(self):
    #     self.mywindow = showFavoriteBrand()
    #     self.mywindow.show()

    # 点击 “修改密码” 按钮
    def clickModifyPassword(self):
        # self.hide()
        self.mywindow = modifyPasswordPage()
        self.mywindow.show()


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    test = personalInfoPage()
    test.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())