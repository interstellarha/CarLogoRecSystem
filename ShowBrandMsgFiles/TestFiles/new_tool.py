# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore
from comp_file import CompTools

class Compview(QtWidgets.QWidget):
    def __init__(self):
        super(Compview, self).__init__()
        self.initUI()
    def initUI(self):
        self.myTools=CompTools(label="data:",content='data path (can drop)',button=u"浏览")
        
        #self.myTools.change_label("path:")
        
        self.myTree=QtWidgets.QTextEdit()
        ok=QtWidgets.QPushButton(u"确定")
        no=QtWidgets.QPushButton(u"取消")
        lbox = QtWidgets.QHBoxLayout()
        lbox.addWidget(ok)
        lbox.addWidget(no)
        
        hbox = QtWidgets.QVBoxLayout()
        hbox.addWidget(self.myTools)
        hbox.addWidget(self.myTree)

        lay=QtWidgets.QVBoxLayout()
        lay.addLayout(hbox)
        lay.addLayout(lbox)
        self.setLayout(lay)
        
        self.setGeometry(250,150,600,450)
        self.setWindowTitle('new widget')   
        #self.show()
 
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Compview()
    ex.show()
    sys.exit(app.exec_())

    
if __name__ == '__main__':
    main()