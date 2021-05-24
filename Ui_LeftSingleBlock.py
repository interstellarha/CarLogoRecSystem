# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LeftSingleBlock.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import src #图片资源


class Ui_LeftSingleBlock(QtWidgets.QWidget):
    '''
        左侧每辆车的模板部件
    '''
    def __init__(self,oneCarList): #传一辆车的参数，一个list
        super(Ui_LeftSingleBlock, self).__init__()
        self.oneCarList = oneCarList
        self.setupUi()

    def setupUi(self):
        # LeftSingleBlock.setObjectName("LeftSingleBlock")
        # LeftSingleBlock.resize(1000, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        # LeftSingleBlock.setMinimumSize(QtCore.QSize(1000, 500))
        # LeftSingleBlock.setMaximumSize(QtCore.QSize(1000, 16777215))
        # LeftSingleBlock.setStyleSheet("")

        self.verticalLayoutWidget = QtWidgets.QWidget()
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 230, 541, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")

        # # 新增layout放背景图，测试能否自由缩放——失败，一个widget只能有一个layout
        # # 新增verticalLayoutWidget_2也不行：不可缩放
        # self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        # self.verticalLayoutWidget_2.setSizePolicy(sizePolicy)
        # self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        # self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        # self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout_5.setObjectName("verticalLayout_5")
        # self.background = QtWidgets.QLabel()
        # self.verticalLayout_5.addWidget(self.background) #增


        self.background = QtWidgets.QLabel(self.widget)
        self.background.setGeometry(QtCore.QRect(0, 0, 535, 121)) #需据不同电脑修改
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())
        self.background.setSizePolicy(sizePolicy)
        self.background.setStyleSheet("border-image: url(:/backSrc/images/leftBlockBackground.jpg);")
        self.background.setText("")
        self.background.setObjectName("background")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.carImg = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carImg.sizePolicy().hasHeightForWidth())
        self.carImg.setSizePolicy(sizePolicy)
        self.carImg.setObjectName("carImg")
        self.horizontalLayout_3.addWidget(self.carImg)

        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.carName = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carName.sizePolicy().hasHeightForWidth())
        self.carName.setSizePolicy(sizePolicy)
        self.carName.setObjectName("carName")
        self.horizontalLayout.addWidget(self.carName)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem1)
        
        self.scoreBar = QtWidgets.QProgressBar()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scoreBar.sizePolicy().hasHeightForWidth())
        self.scoreBar.setSizePolicy(sizePolicy)
        self.scoreBar.setMinimumSize(QtCore.QSize(100, 20))
        self.scoreBar.setMaximumSize(QtCore.QSize(100, 20))
        self.scoreBar.setMaximum(100)
        self.scoreBar.setProperty("value", 51)
        self.scoreBar.setTextVisible(True)
        self.scoreBar.setOrientation(QtCore.Qt.Horizontal)
        self.scoreBar.setInvertedAppearance(False)
        self.scoreBar.setObjectName("scoreBar")
        self.verticalLayout_3.addWidget(self.scoreBar)

        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem2)

        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.levelLabel = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.levelLabel.sizePolicy().hasHeightForWidth())
        self.levelLabel.setSizePolicy(sizePolicy)
        self.levelLabel.setObjectName("levelLabel")
        self.horizontalLayout_2.addWidget(self.levelLabel)

        self.level = QtWidgets.QLabel()
        self.level.setObjectName("level")
        self.horizontalLayout_2.addWidget(self.level)
        self.engineLabel = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.engineLabel.sizePolicy().hasHeightForWidth())

        self.engineLabel.setSizePolicy(sizePolicy)
        self.engineLabel.setObjectName("engineLabel")
        self.horizontalLayout_2.addWidget(self.engineLabel)

        self.engine = QtWidgets.QLabel()
        self.engine.setObjectName("engine")
        self.horizontalLayout_2.addWidget(self.engine)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.line_3 = QtWidgets.QFrame()
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.verticalLayout_2.addWidget(self.line_3)
        self.verticalLayout_4.addWidget(self.widget)

        self.retranslateUi()
        
        self.setLayout(self.verticalLayout_4)

        # QtCore.QMetaObject.connectSlotsByName(LeftSingleBlock)

    def retranslateUi(self):
        self.carImg.setText("TextLabel")
        self.carName.setText("TextLabel")
        self.label.setText("用户评分：")
        self.scoreBar.setFormat("%v") #进度条右侧显示值评分值0~100
        self.levelLabel.setText("级别：")
        self.level.setText("TextLabel")
        self.engineLabel.setText("发动机：")
        self.engine.setText("TextLabel")

        self.carName.setText('<a href="{}">{}</a>' .format(self.oneCarList[-1],self.oneCarList[0])) #车名
        self.carName.setOpenExternalLinks(True)  # 使成为超链接，外部浏览器打开

        url = self.oneCarList[1] #车图片
        req = requests.get(url)
        carPhoto = QtGui.QPixmap()
        carPhoto.loadFromData(req.content)
        carPhoto = carPhoto.scaled(QtCore.QSize(160,120)) #4:3
        self.carImg.setPixmap(carPhoto)

        #问题：print(type(self.oneCarList[2])) #str
        if(self.oneCarList[2]):
            score = self.oneCarList[2]
            if(score.isspace()): #去掉评分中的空格
                score = score.replace(' ','')
            #print(score.isspace())
            if(score == ""):
                score = 0
            self.scoreBar.setValue(float(score) * 100 / 5) #评分:0~100
        else:
            self.scoreBar.setValue(0)
        self.level.setText(self.oneCarList[3]) #级别
        self.engine.setText(self.oneCarList[4]) #引擎

# 仅为测试
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_LeftSingleBlock(['奥迪A3', 'http://car3.autoimg.cn/cardfs/product/g30/M02/25/C0/120x90_0_q95_autohomecar__ChsEoF-pNuOAZzDzACTok2HOnoI585.jpg', '4.56', '紧凑型车', '1.4T'])
    ex.show()
    sys.exit(app.exec_())

# 仅为测试
if __name__ == '__main__':
    main()