# @Author: 童颖睿
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QAction, QScrollArea
from PyQt5.QtCore import *
import sys
import sqlite3
import requests
import globalvar as gl
from _basicBrandBlock import Ui_BrandBlock

# note when run on whole
gl._init()

class Ui_LikeBrands(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_LikeBrands, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        """得到当前登录用户的用户名"""
        username = gl.get_value('username')
        print(username)

        self.conn = sqlite3.connect("database.db")  # 连接数据库
        self.cursor = self.conn.cursor()
        sql = ''' SELECT brand from ILIKE where userName = ? '''  # 从数据库查询我喜欢的品牌

        self.cursor.execute(sql, (username,))
        self.likeBrands = self.cursor.fetchall()  # 所有
        self.row = len(self.likeBrands)  # 取得记录个数，用于设置表格的行数
        print(self.row)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # new
        self.TableBrands = QtWidgets.QTableWidget(MainWindow)
        self.TableBrands.setContentsMargins(0, 0, 0, 0)
        self.TableBrands.setGeometry(QtCore.QRect(10, 10, 981, 646))
        self.TableBrands.setObjectName("verticalLayout")
        self.TableBrands.setColumnCount(4)
        self.TableBrands.setRowCount(self.row / 4 + 1)
        self.TableBrands.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.TableBrands.horizontalHeader().setVisible(False)  # 隐藏水平表头
        self.TableBrands.setShowGrid(False)

        self.addLikeBrands()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addLikeBrands(self):
        for i in range(self.row):  # 循环每个喜欢品牌
            item = self.likeBrands[i]
            self.brand = Ui_BrandBlock(item)
            self.TableBrands.setCellWidget(int(i / 4), i % 4, self.brand)
            self.TableBrands.setColumnWidth(i % 4, 200)  # 设置列的宽度
            self.TableBrands.setRowHeight(int(i / 2), 200)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "我喜欢的品牌"))

if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    showLikeBrands = Ui_LikeBrands()
    showLikeBrands.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())