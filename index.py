# -*- coding: utf-8 -*-
# @Time: 2021/5/16 11:14
# @Author: 车诗琪
# @File: index
# @Project: HWprogram
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

from index_ui import Ui_index
from PyQt5.QtGui import *
from search import Ui_MainWindow

class FormIndex(QWidget, Ui_index):
    def __init__(self, parent=None):
        super(FormIndex, self).__init__(parent)
        self.setupUi(self)
        self.carLogo.clicked.connect(self.carLogoClicked)

    def carLogoClicked(self):
        self.hide()
        self.MainWindow = QMainWindow()
        self.test = Ui_MainWindow()
        self.test.setupUi(self.MainWindow)
        self.MainWindow.show()


if __name__ == '__main__':
    #QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    dialog = FormIndex()
    dialog.show()
    sys.exit(app.exec_())
