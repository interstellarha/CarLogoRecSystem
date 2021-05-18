# -*- coding: utf-8 -*-
# @Time: 2021/5/14 21:20
# @Author: 车诗琪
# @File: login
# @Project: HWprogram
import sys
import os
import sqlite3  # 用于数据库
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QAction, QLineEdit, QMainWindow
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QIcon
from login_ui import Ui_login
from register import FormSignUp
from index import FormIndex
import globalvar as gl

gl.set_value('username', "")  # 设置变量值 username

def common(cn, sql):
    """将数据从sql格式转换成列表镶嵌字典的格式并返回"""
    cursor = cn.execute(sql)
    information = []
    for row in cursor:
        information.append(row)
    return information


def judge_account(account):
    """用于判断账号是否存在"""
    cn = sqlite3.connect("database.db")
    sql = '''SELECT DISTINCT name
             FROM user
          '''
    aaccounts = common(cn, sql)
    for acc in aaccounts:
        if acc[0] == account:
            return 1  # 返回1说明账号存在
    return 0


def judge_ac_and_pw( account, password):
    """用于判断账号和密码是否匹配"""
    cn = sqlite3.connect("database.db")
    cursor = cn.cursor()
    sql = '''SELECT DISTINCT name, pwd
             FROM user WHERE name=?
          '''
    result = cursor.execute(sql, (account,))
    data = result.fetchall()
    if account and password:  # 如果两个都不空
        if data:
            if str(data[0][1]) == password:
                return 1
            else:
                return 0


class FormSignIn(QMainWindow, Ui_login):
    def __init__(self, parent=None):
        super(FormSignIn, self).__init__(parent)
        self.setupUi(self)

        ## 绑定按钮事件
        self.logIn.clicked.connect(self.on_button_login)
        self.cancel.clicked.connect(self.on_button_cancel)

    def on_button_cancel(self):
        self.close()

    def on_button_login(self):  # 按下“登录”的按钮
        account = self.lineEdit_account.text()

        count = judge_account(account)
        if count != 1:
            reply = QMessageBox.warning(self, "警告", "账号不存在，请重新输入", QMessageBox.Retry, QMessageBox.Retry)
            if reply == QMessageBox.Retry:
                self.lineEdit_account.clear()
                self.lineEdit_password.clear()
        else:
            password = self.lineEdit_password.text()
            count = judge_ac_and_pw(account, password)
            if count == 1:
                reply = QMessageBox.information(self, '恭喜', '登录成功!', QMessageBox.Ok, QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    self.hide()
                    self.mywindow = FormIndex()
                    gl.set_value('username', account)  # 设置变量值 user
                    self.mywindow.show()
            else:
                reply = QMessageBox.warning(self, "警告", "密码错误", QMessageBox.Retry, QMessageBox.Retry)
                if reply == QMessageBox.Retry:
                    self.lineEdit_password.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    signin = FormSignIn()
    signup = FormSignUp()
    signin.show()
    signin.register_2.clicked.connect(signup.show)
    sys.exit(app.exec_())
