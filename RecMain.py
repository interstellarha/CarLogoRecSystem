import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Recognizing import Ui_Recognizing
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
#from predict import result

global OpenFilePath
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
        #print(OpenFilePath)

    #def recognizing(self):
     #   print(result)


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    m = SelectWin()
    m.select.clicked.connect(m.openImage)
    print(OpenFilePath)
    #m.recognize.clicked.connect(m.recognizePath(m.OpenFilePath))
    m.show()
    '''
    MainWindow = QMainWindow()
    ui = Ui_Recognizing()
    ui.setupUi(MainWindow)
    MainWindow.show()
    '''
    sys.exit(app.exec_())
