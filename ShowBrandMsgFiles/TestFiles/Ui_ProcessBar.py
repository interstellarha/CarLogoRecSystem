import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt5.QtCore import QBasicTimer

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('开始', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('进度条')
        self.show()

    def timerEvent(self, e):

        if self.step >= 100:
            self.step = 0
            self.pbar.setValue(self.step)
            self.timer.stop() #结束停止
            self.btn.setText('完成')
            return
        self.step = self.step+1
        self.pbar.setValue(self.step)

    def doAction(self, value):
        print("do action")
        if self.timer.isActive(): #默认打开
            self.timer.stop() #点一次停止
            self.btn.setText('开始')
        else:
            self.timer.start(100, self) #再点击打开
            self.btn.setText('停止') 

if __name__ == '__main__':
     app = QApplication(sys.argv)
     ex = Example()
     sys.exit(app.exec_())