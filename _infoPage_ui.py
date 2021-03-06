# @Author: 童颖睿

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog,QMessageBox,QAction
from PyQt5.QtCore import *

import globalvar as gl


class Ui_Info(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("#MainWindow{border-image:url(./carImg/bg1.jpg);}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 60, 421, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 31))

        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(150, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)

        # 用户名
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(60, 140, 371, 300))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(120, 10, 200, 200))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.graphicsView = QtWidgets.QGraphicsView(self.frame_5)
        # self.graphicsView.setObjectName("graphicsView")

        #头像框
        self.label_icon = QtWidgets.QLabel(self.frame_5)
        self.label_icon.setGeometry(QtCore.QRect(0, 120, 200, 200))
        self.label_icon.setObjectName("label_icon")
        self.verticalLayout_2.addWidget(self.label_icon)

        #显示用户头像
        username = gl.get_value('username')
        img = QtGui.QPixmap("./sqlite_create/" + str(username) + ".jpg").scaled(QtCore.QSize(200, 175))
        self.label_icon.setPixmap(img)

        self.changePortrait = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.changePortrait.setFont(font)
        self.changePortrait.setObjectName("changePortrait")
        # self.changePortrait.setGeometry(QtCore.QRect(60, 330, 371, 100))
        self.verticalLayout_2.addWidget(self.changePortrait)

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(60, 330, 371, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(130, 55, 241, 60))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)

        # 注册时间
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(330, 460, 131, 101))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.favoriteBrand = QtWidgets.QPushButton(self.centralwidget)
        self.favoriteBrand.setGeometry(QtCore.QRect(580, 460, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.favoriteBrand.setFont(font)
        self.favoriteBrand.setObjectName("favoriteBrand")
        self.modifyPassword = QtWidgets.QPushButton(self.centralwidget)
        self.modifyPassword.setGeometry(QtCore.QRect(580, 520, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.modifyPassword.setFont(font)
        self.modifyPassword.setObjectName("modifyPassword")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("个人主页")
        self.label.setText( "用户名")
        self.label_5.setText(str(gl.get_value('username')))
        self.label_2.setText("头像")
        self.changePortrait.setText("更改头像")
        self.label_3.setText("注册时间")
        self.label_4.setText(str(gl.get_value('registerTime')))
        self.favoriteBrand.setText("我喜欢的品牌")
        self.modifyPassword.setText("修改密码")


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    test = Ui_Info()
    test.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
