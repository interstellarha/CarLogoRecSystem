from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
from bs4 import BeautifulSoup
from left_table import *


class MainWindow(QMainWindow,Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())