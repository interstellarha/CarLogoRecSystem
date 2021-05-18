# -*- coding: utf-8 -*-
# @Time: 2021/5/16 11:14
# @Author: 车诗琪
# @File: index
# @Project: HWprogram
import sys

from PyQt5.QtWidgets import QApplication, QWidget

from index_ui import Ui_index

from _infoPage import personalInfoPage


class FormIndex(QWidget, Ui_index):
    def __init__(self, parent=None):
        super(FormIndex, self).__init__(parent)
        self.setupUi(self)
        self.home.clicked.connect(self.enterHomePage)

    def enterHomePage(self):
        self.hide()
        self.mywindow = personalInfoPage()
        self.mywindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = FormIndex()
    dialog.show()
    sys.exit(app.exec_())