from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog,QMessageBox,QAction
import sys
import sqlite3



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        # MainWindow.setStyleSheet("#MainWindow{border-image:url(background.jpg)}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.msg = QtWidgets.QLabel(self.centralwidget)
        self.msg.setGeometry(QtCore.QRect(150, 30, 400, 50))
        self.msg.hide()


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 100, 400, 50))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Input Brand of Car")
        self.lineEdit.setStyleSheet("border:2px solid rgba(52,128,175,255);border-radius:10px;padding:2px 4px")

        self.searchAction = QAction(self.lineEdit)
        self.searchAction.setIcon(QtGui.QIcon("images/sear.PNG"))
        self.searchAction.triggered.connect(self.search)
        self.lineEdit.addAction(self.searchAction,QtWidgets.QLineEdit.TrailingPosition)

        '''self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 100, 50, 50))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("border-image:url(./images/sear.PNG);")
        self.pushButton.clicked.connect(self.pushButtonClicked)'''


        self.logolist = QtWidgets.QTableWidget(self.centralwidget)           
        self.logolist.setGeometry(QtCore.QRect(150, 175, 400, 200))
        self.logolist.verticalHeader().setVisible(False)       # 隐藏垂直表头
        self.logolist.horizontalHeader().setVisible(False)     # 隐藏水平表头
        self.logolist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)   # 隐藏垂直滚动条
        self.logolist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)     # 隐藏水平滚动条
        self.logolist.setColumnCount(4)
        self.logolist.setRowCount(2)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 175, 400, 200))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutWidget.hide()

   
        for i in range(8):
            icon = QtWidgets.QLabel()
            icon.setMargin(4)
            img = QtGui.QPixmap("./images/"+str(i)+".PNG").scaled(QtCore.QSize(80, 80))
            icon.setPixmap(img)
            self.logolist.setCellWidget(int(i/4), i%4, icon)
            self.logolist.setColumnWidth(i%4, 100)          # 设置列的宽度
            self.logolist.setRowHeight(int(i/2), 100)       # 设置行的高

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    
    def search(self):
        text = self.lineEdit.text()
        if len(text)== 0:
            self.msg.setText("Please Input a Brand")
            self.msg.show()
        else:
            self.msg.hide()
            self.logolist.hide()
            logolabel = QtWidgets.QLabel("Logo:")
            logo = QtWidgets.QLabel()
            img = QtGui.QPixmap("./images/1.PNG").scaled(QtCore.QSize(80, 80))
            logo.setPixmap(img)

            brandlabel = QtWidgets.QLabel("Brand:")
            brandmsg = QtWidgets.QTextEdit()
            brandmsg.setReadOnly(True)

            followlabel = QtWidgets.QLabel("Followers:")
            followmsg = QtWidgets.QLabel("4")

            self.gridLayout.setSpacing(10)
            self.gridLayout.addWidget(logolabel,1,0)
            self.gridLayout.addWidget(logo,1,1)

            self.gridLayout.addWidget(brandlabel,2,0)
            self.gridLayout.addWidget(brandmsg,2,1)

            self.gridLayout.addWidget(followlabel,3,0)
            self.gridLayout.addWidget(followmsg,3,1)
            self.gridLayoutWidget.show()
        
         
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    test = Ui_MainWindow()
    test.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

