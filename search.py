from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog,QMessageBox,QAction
import sys
import sqlite3
import requests
import globalvar as gl


gl._init()

class Ui_MainWindow(object):
    def __init__(self):
        self.userName = gl.get_value('username')
        # print(self.userName)
        self.database = sqlite3.connect('database.db')
        self.c = self.database.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS COMMENT (userName text not null, cname varchar not null, comment text not null)")
        self.database.commit()
        self.brand = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("#MainWindow{border-image:url(./images/background.png);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 提示信息
        self.msg = QtWidgets.QLabel(self.centralwidget)
        self.msg.setGeometry(QtCore.QRect(150, 150, 400, 50))
        self.msg.hide()
        # 返回home页面
        self.backToHome = QtWidgets.QPushButton(self.centralwidget)
        self.backToHome.setGeometry(QtCore.QRect(50, 53, 50, 50))
        self.backToHome.setStyleSheet("border-image: url(./images/home.png);border:2px;border-radius:5px;padding:2px 4px;")
        # 数据库
        self.database = sqlite3.connect('database.db')
        self.c = self.database.cursor()
        # 搜索输入框
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 53, 500, 50))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Input Brand of Car")
        self.lineEdit.setStyleSheet("border:2px solid rgba(52,128,175,255);border-radius:10px;padding:2px 4px")
        # 搜索动作
        self.searchAction = QAction(self.lineEdit)
        self.searchAction.setIcon(QtGui.QIcon("images/sear.PNG"))
        self.searchAction.triggered.connect(self.search)
        self.lineEdit.addAction(self.searchAction,QtWidgets.QLineEdit.TrailingPosition)
        # 返回动作
        self.backAction = QAction(self.lineEdit)
        self.backAction.setIcon(QtGui.QIcon("images/back.PNG"))
        self.backAction.triggered.connect(self.back)
        self.lineEdit.addAction(self.backAction,QtWidgets.QLineEdit.LeadingPosition )

        '''self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 100, 50, 50))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("border-image:url(./images/sear.PNG);")
        self.pushButton.clicked.connect(self.pushButtonClicked)'''

        # 显示logo
        self.logolist = QtWidgets.QTableWidget(self.centralwidget)           
        self.logolist.setGeometry(QtCore.QRect(185, 175, 430, 400))
        self.logolist.verticalHeader().setVisible(False)       # 隐藏垂直表头
        self.logolist.horizontalHeader().setVisible(False)     # 隐藏水平表头
        self.logolist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)   # 隐藏水平滚动条
        self.logolist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn) # 开启垂直滚动条
        self.logolist.setShowGrid(False)
        self.logolist.verticalScrollBar().setStyleSheet("QScrollBar::handle{background:lightgray; border:2px solid transparent;border-radius:5px;}")
        self.logolist.setColumnCount(4)
        self.logolist.setRowCount(10)
        self.logolist.setStyleSheet("border:none")
        self.logolist.cellClicked.connect(self.logoClicked)

        # 显示品牌信息
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        #self.scrollbar = QtWidgets.QScrollBar(Qt.Vertical, self.widget)
        #self.scrollbar.setMaximum(900) 
        self.gridLayoutWidget.setGeometry(QtCore.QRect(27, 120, 360, 453))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        logolabel = QtWidgets.QLabel("Logo")
        logolabel.setStyleSheet("QLabel{font-size:20px;font-weight:normal;font-family:Arial;}")
        brandlabel = QtWidgets.QLabel("Brand")
        brandlabel.setStyleSheet("QLabel{font-size:20px;font-weight:normal;font-family:Arial;}")
        followlabel = QtWidgets.QLabel("Followers")
        followlabel.setStyleSheet("QLabel{font-size:20px;font-weight:normal;font-family:Arial;}")
        self.gridLayout.addWidget(logolabel,1,0)
        self.gridLayout.addWidget(followlabel,1,3)
        self.gridLayout.addWidget(brandlabel,2,0)

        self.gridLayoutWidget.hide()
        
        #添加评论按钮
        self.comment = QtWidgets.QLineEdit(self.centralwidget)
        self.comment.setGeometry(QtCore.QRect(413, 120, 360, 33))
        self.comment.setObjectName("comment")
        self.comment.setPlaceholderText("Say Something~")
        self.comment.setStyleSheet("border:1px black")

        self.commectAction = QAction(self.comment)
        self.commectAction.setIcon(QtGui.QIcon("images/comment.jpg"))
        self.commectAction.triggered.connect(self.commentAdd)
        self.comment.addAction(self.commectAction,QtWidgets.QLineEdit.TrailingPosition)
        self.comment.hide()

        # 显示评论
        self.commentText = QtWidgets.QTextEdit(self.centralwidget)
        self.commentText.setReadOnly(True)
        self.commentText.setGeometry(QtCore.QRect(413, 167, 360, 407))
        self.commentText.hide()

        # logo和品牌的字典
        self.logoToBrand = {}
        # 从数据库中查询logo的图片地址和名称
        self.c.execute("SELECT cname from CAR_BRAND")
        result = self.c.fetchall()
        # 显示品牌logo
        for i in range(40):
            self.logoToBrand[i] = result[i][0]
            icon = QtWidgets.QLabel()
            icon.setMargin(4)
            #url = result[i][0]
            #res = requests.get(url)
            #img = QtGui.QImage.fromData(res.content)
            if (i==22) or (i==26):
                img = QtGui.QPixmap("./images/"+str(i)+".PNG")
            else:
                img = QtGui.QPixmap("./images/"+str(i)+".jpg")
            icon.setPixmap(img.scaled(QtCore.QSize(80, 80)))
            icon.setStyleSheet("border:2px solid rgba(52,128,175,255);border-radius:10px;padding:2px 4px")
            self.logolist.setCellWidget(int(i/4), i%4, icon)
            self.logolist.setColumnWidth(i%4, 100)          # 设置列的宽度
            self.logolist.setRowHeight(int(i/4), 100)       # 设置行的高


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

    # 搜索动作绑定的函数
    def search(self):
        text = self.lineEdit.text()
        if len(text) == 0:
            reply = QMessageBox.warning(self.centralwidget, "Hint", "Please Input a Brand!", QMessageBox.Retry, QMessageBox.Retry)
            if reply == QMessageBox.Retry:
                self.lineEdit.clear()
        else:
            self.c.execute("SELECT * from CAR_BRAND where cname = \"{Cname}\" OR ename = \"{Cname}\"".format(Cname=text))
            result = self.c.fetchone()

            self.msg.hide()
            self.logolist.hide()
            if result == None:
                self.msg.setText("Sorry! Nothing Found!")
                self.msg.show()
            else:
                self.brand = result[0]
                logo = QtWidgets.QLabel()
                url = result[2]
                res = requests.get(url)
                img = QtGui.QImage.fromData(res.content)
                logo.setPixmap(QtGui.QPixmap.fromImage(img).scaled(QtCore.QSize(60, 60)))

                brandmsg = QtWidgets.QTextEdit()
                brandmsg.setText(result[3])
                brandmsg.setReadOnly(True)

                followmsg = QtWidgets.QLineEdit()
                followmsg.setReadOnly(True)
                followmsg.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px")
                followmsg.setAlignment(Qt.AlignCenter)
                self.c.execute("SELECT * from ILIKE where brand = \"{Cname}\"".format(Cname=result[0]))
                followResult = self.c.fetchall()
                followmsg.setText(str(len(followResult)))

                self.gridLayout.setSpacing(10)
                self.gridLayout.addWidget(logo,1,1)

                self.gridLayout.addWidget(followmsg,1,4)

                self.gridLayout.addWidget(brandmsg,2,1,3,4)
                self.gridLayoutWidget.show()
                self.comment.show()
                self.commentShow()
                self.commentText.show()

    # back动作绑定的函数：返回logo显示页面
    def back(self):
        self.msg.hide()
        self.gridLayoutWidget.hide()
        self.comment.hide()
        self.commentText.hide()
        self.lineEdit.setText("")
        self.logolist.show()
    
    def commentAdd(self):
        text = self.comment.text()
        if len(text)!=0:
            print("评论：")
            print(text)
            self.c.execute("INSERT INTO COMMENT (userName, cname, comment) values (\"{USERNAME}\",\"{CNAME}\",\"{COMMENT}\")".format(USERNAME = self.userName, CNAME = self.brand, COMMENT = text))
            self.database.commit()
            self.commentShow()
        else:
            return
    
    def commentShow(self):
        self.c.execute("SELECT * from COMMENT where cname = \"{CNAME}\"".format(CNAME = self.brand))
        commentResult = self.c.fetchall()
        self.commentText.clear()
        if commentResult != None:
            for i in range(len(commentResult)):
                username = commentResult[i][0]
                # print(username)
                userComment = commentResult[i][2]
                self.commentText.moveCursor(QtGui.QTextCursor.End)
                self.commentText.setTextColor(QtGui.QColor(70,130,180))
                self.commentText.insertPlainText(username+"\n")
                self.commentText.setTextColor(Qt.black)
                self.commentText.insertPlainText(userComment+"\n")

    
    # 点击某一个logo绑定的函数
    def logoClicked(self,row,column):
        self.logolist.hide()
        CNAME = self.logoToBrand[row*4+column]
        print(CNAME)
        self.brand = CNAME
        self.c.execute("SELECT * from CAR_BRAND where cname = \"{Cname}\"".format(Cname = CNAME))
        brandInfo = self.c.fetchone()
        logo = QtWidgets.QLabel()
        url = brandInfo[2]
        res = requests.get(url)
        img = QtGui.QImage.fromData(res.content)
        logo.setPixmap(QtGui.QPixmap.fromImage(img).scaled(QtCore.QSize(60, 60)))

        brandmsg = QtWidgets.QTextEdit()
        brandmsg.setText(brandInfo[3])
        brandmsg.setReadOnly(True)
        brandmsg.setStyleSheet("border:none")

        followmsg = QtWidgets.QLineEdit()
        followmsg.setReadOnly(True)
        followmsg.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px")
        followmsg.setAlignment(Qt.AlignCenter)
        self.c.execute("SELECT * from ILIKE where brand = \"{Cname}\"".format(Cname=brandInfo[0]))
        followResult = self.c.fetchall()
        followmsg.setText(str(len(followResult)))

        self.gridLayout.setSpacing(10)
        self.gridLayout.addWidget(logo,1,1)
        self.gridLayout.addWidget(followmsg,1,4)
        self.gridLayout.addWidget(brandmsg,2,1,3,4)
        self.gridLayoutWidget.show()
        self.comment.show()
        self.commentShow()
        self.commentText.show()
        
         
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    test = Ui_MainWindow()
    test.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
