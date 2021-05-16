# -*- coding: utf-8 -*-
# @Time: 2021/5/15 15:20
# @Author: 车诗琪
# @File: register
# @Project: HWprogram
import base64
import sys
import os
import sqlite3  # 用于数据库
from datetime import time

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QAction, QLineEdit, QMainWindow, QLabel
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QIcon
from register_ui import Ui_regist


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


class FormSignUp(QWidget, Ui_regist):
    def __init__(self, parent=None):
        super(FormSignUp, self).__init__(parent)
        self.setupUi(self)
        # self.lineEdit_name.editingFinished.connect(self.confirm_name)
        self.all_validator()  # 正则表达式不能和editingFinished()一起用

        ## 绑定按钮事件
        self.register_2.clicked.connect(self.on_button_signup)
        self.cancel.clicked.connect(self.on_button_cancel)

    def on_button_cancel(self):
        self.close()

    def on_button_signup(self):  # 按下“注册”的按钮
        # self.confirm_name()
        # if self.name_count == 0:
        self.confirm_account()
        if self.account_count == 0:
            self.confirm_password()

        if self.account_count == 0 \
                and self.password_count == 0:
            self.add_account()
            action = QAction(self)  # 给账号加√按钮
            action.setIcon(QIcon("./pyqtpic/check.png"))
            action.triggered.connect(self.action_confirm_account)
            self.lineEdit_account.addAction(action, QLineEdit.TrailingPosition)

            reply = QMessageBox.information(self, '恭喜', '注册成功!',
                                            QMessageBox.Ok, QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                self.hide()

    def all_validator(self):  # 账号和密码的正则表达式
        regx = QRegExp("^[0-9A-Za-z]{14}$")

        validator2 = QRegExpValidator(regx, self.lineEdit_password)
        self.lineEdit_password.setValidator(validator2)
        validator3 = QRegExpValidator(regx, self.lineEdit_confirmpassword)
        self.lineEdit_confirmpassword.setValidator(validator3)

    '''''
    def confirm_name(self):
        """确认用户名是否为正确格式"""
        self.tip_name.setText("建议为姓名")
        self.tip_name.setStyleSheet("color:black;")
        self.name_count = 0

        name = self.lineEdit_account.text()
        if len(name) == 0:
            QMessageBox.warning(self, "警告", "用户名为空")
            self.tip_name.setText("用户名为空")
            self.tip_name.setStyleSheet("color:red;")  # 把标签信息修改为红色
            self.name_count = 1
    '''''

    def confirm_account(self):
        """确认账号是否存在"""
        account_str = "由数字、字母或汉字组成"
        self.tip_account.setText(account_str)
        self.tip_account.setStyleSheet("color:white;")
        self.account_count = 0

        account = self.lineEdit_account.text()
        if len(account) == 0:
            account_str = "账号为空"
            action = QAction(self)  # 给账号加√按钮
            action.setIcon(QIcon("./pyqtpic/check-1.png"))
            action.triggered.connect(self.action_confirm_account)
            self.lineEdit_account.addAction(action, QLineEdit.TrailingPosition)

        else:
            count = judge_account(account)  # 在数据库中查找是否有相同的账号
            if count == 1:
                account_str = "账号已存在"
                action = QAction(self)  # 给账号加√按钮
                action.setIcon(QIcon("./pyqtpic/check-1.png"))
                action.triggered.connect(self.action_confirm_account)
                self.lineEdit_account.addAction(action, QLineEdit.TrailingPosition)

        if account_str != "由数字、字母或汉字组成":
            QMessageBox.warning(self, "警告", account_str)
            self.tip_account.setText(account_str)
            self.tip_account.setStyleSheet("color:red;")  # 把标签信息修改为红色
            self.account_count = 1

    def action_confirm_account(self):
        """在动作上多加一个成功提示框"""
        self.confirm_account()
        if self.account_count == 0:
            QMessageBox.information(self, '恭喜', '该账号可以使用!')

    def confirm_password(self):
        """确认密码是否为正确格式"""
        self.tip_password.setText("长度为6-15位，由数字和字母组成")
        self.tip_confirmpassword.setText("再次确认密码")
        self.tip_password.setStyleSheet("color:white;")
        self.tip_confirmpassword.setStyleSheet("color:white;")
        self.password_count = 0

        password = self.lineEdit_password.text()
        con_password = self.lineEdit_confirmpassword.text()
        if len(password) == 0:
            QMessageBox.warning(self, "警告", "密码为空")
            self.tip_password.setText("密码为空")
            self.tip_password.setStyleSheet("color:red;")
            self.password_count = 1
        elif len(password) < 6:
            QMessageBox.warning(self, "警告", "密码长度低于6位")
            self.tip_password.setText("密码长度低于6位")
            self.tip_password.setStyleSheet("color:red;")
            self.password_count = 1
        elif password != con_password:
            reply = QMessageBox.critical(self, '错误', '两次输入的密码不一致',
                                         QMessageBox.Retry, QMessageBox.Retry)
            self.tip_confirmpassword.setText("两次输入的密码不一致")
            self.tip_confirmpassword.setStyleSheet("color:red;")  # 把标签信息修改为红色
            if reply == QMessageBox.Retry:
                self.lineEdit_password.clear()
                self.lineEdit_confirmpassword.clear()
                self.password_count = 1

    def add_account(self):
        """注册成功后的操作"""
        name = self.lineEdit_account.text()  # 将新注册的账号录入系统的账号数据库
        password = self.lineEdit_password.text()

        cn = sqlite3.connect("database.db")  # 连接系统账号数据库
        cursor = cn.cursor()
        c = cursor.execute('''select * from user''')
        r = c.fetchall()
        num = len(r) + 1

        sql = '''insert into user(id,name,pwd) 
                            values( '%s', '%s','%s')
                         ''' % (num, name, password)
        cn.execute(sql)
        cn.commit()

        #with open("./pyqtpic/portrait.jpg", "rb") as f:
            #res = base64.b64encode(f.read())
            #sql = '''insert into user(portrait) values(?)''' % (res,)
            #cn.execute(sql)
            #cn.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = FormSignUp()
    dialog.show()
    sys.exit(app.exec_())
