import sys
from PyQt5.QtWidgets import *
 
 
class MainWindow(QMainWindow):
    def __init__(self,):
        super(QMainWindow,self).__init__()
        self.number = 0
 
        w = QWidget()
        self.setCentralWidget(w)
 
        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(250, 2000)#######设置滚动条的尺寸
        for filename in range(20):
            self.MapButton = QPushButton(self.topFiller)
            self.MapButton.setText(str(filename))
            self.MapButton.move(10,filename*40)

        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topFiller)
 
 # 滚动里的每行加到文件部件
 # 文件部件加到滚动框，文件部件设置大小
 # 滚动框放到vbox
 # vbox放到主界面
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        w.setLayout(self.vbox)
 
        self.statusBar().showMessage("底部信息栏")
        self.resize(300, 500)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
