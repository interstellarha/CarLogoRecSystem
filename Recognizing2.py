# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Recognizing2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Recognizing2(object):
    def setupUi(self, Recognizing2):
        Recognizing2.setObjectName("Recognizing2")
        Recognizing2.resize(790, 441)
        # Recognizing2.setStyleSheet("#frame{border-image: url(:/pyqtpic/recommend.jpg);}")
        # self.frame = QtWidgets.QFrame(Recognizing2)
        # self.frame.setGeometry(QtCore.QRect(0, 0, 780, 441))
        # self.frame.setStyleSheet("")
        # self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        # self.frame.setObjectName("frame")
        self.recommendback = QtWidgets.QLabel(Recognizing2)
        self.recommendback.setGeometry(QtCore.QRect(0, 0, 790, 441))
        self.recommendback.setStyleSheet("border-image: url(./pyqtpic/recommend.jpg);")
        self.recommendback.setText("")
        self.recommendback.setObjectName("recommendbackground")
        self.name = QtWidgets.QLabel(Recognizing2)
        self.name.setGeometry(QtCore.QRect(640, 10, 131, 41))
        self.name.setStyleSheet("background-color: rgb(255, 255,255, 0);\n"
"font: 14pt \"Arial\";")
        self.name.setText("")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.iLike = QtWidgets.QPushButton(Recognizing2)
        self.iLike.setGeometry(QtCore.QRect(670, 60, 75, 23))
        self.iLike.setStyleSheet("border-image: url(./pyqtpic/cancel.png);\n"
" rgb(255, 255,255, 0);\n"
"}")
        self.iLike.setObjectName("iLike")
        self.back = QtWidgets.QPushButton(Recognizing2)
        self.back.setGeometry(QtCore.QRect(10, 10, 31, 23))
        self.back.setObjectName("back")
        self.likeShow = QtWidgets.QLabel(Recognizing2)
        self.likeShow.setGeometry(QtCore.QRect(650, 90, 121, 31))
        self.likeShow.setStyleSheet("font: 11pt \"Arial\";")
        self.likeShow.setText("")
        self.likeShow.setAlignment(QtCore.Qt.AlignCenter)
        self.likeShow.setObjectName("likeShow")
        self.scrollArea_2 = QtWidgets.QScrollArea(Recognizing2)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 40, 520, 391))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        # self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        #self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 522, 3000))
        #self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(0, 3000))
        # self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Recognizing2)

        #self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)

        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        #swf：尝试加背景
        self.verticalLayoutWidget2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        #self.verticalLayoutWidget2.setGeometry(QtCore.QRect(10, 10, 160, 80))
        self.verticalLayoutWidget2.setObjectName("verticalLayoutWidget2")
        self.verticalLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout2.setObjectName("verticalLayout2")

        self.scrollArea_2.setWidget(self.verticalLayoutWidget)
        self.origin = QtWidgets.QLabel(Recognizing2)
        self.origin.setGeometry(QtCore.QRect(560, 10, 61, 51))
        self.origin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.origin.setText("")
        self.origin.setObjectName("origin")
        self.pic = QtWidgets.QLabel(Recognizing2)
        self.pic.setGeometry(QtCore.QRect(560, 70, 61, 51))
        self.pic.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pic.setText("")
        self.pic.setObjectName("pic")
        self.textBrowser = QtWidgets.QTextBrowser(Recognizing2)
        self.textBrowser.setGeometry(QtCore.QRect(580, 130, 201, 301))
        self.textBrowser.setObjectName("textBrowser")

        self.message = QtWidgets.QLabel(Recognizing2)
        self.message.setGeometry(QtCore.QRect(130, 90, 200, 200))
        self.message.setStyleSheet("font: 20pt \"Arial Rounded MT Bold\";")
        self.message.setObjectName("label")

        self.retranslateUi(Recognizing2)
        QtCore.QMetaObject.connectSlotsByName(Recognizing2)

    def retranslateUi(self, Recognizing2):
        _translate = QtCore.QCoreApplication.translate
        Recognizing2.setWindowTitle(_translate("Recognizing2", "Recognizing2"))
        self.iLike.setText(_translate("Recognizing2", "like"))
        self.back.setText(_translate("Recognizing2", "<"))
        self.message.setText(_translate("Form", "暂无推荐信息"))  # 英文名

