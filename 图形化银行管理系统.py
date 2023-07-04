
# -*- coding: utf-8 -*-

# 导入 PyQt5 模块中的 QtWidgets 组件
from PyQt5 import QtCore, QtGui, QtWidgets


# 生成界面类
class Ui_Dialog(object):
    # 设置界面元素属性
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton1 = QtWidgets.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(120, 190, 81, 31))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 190, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(160, 50, 111, 21))
        self.label1.setObjectName("label1")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(120, 100, 191, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(120, 140, 191, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 100, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 31, 31))
        self.label_2.setObjectName("label_2")

        # 填写界面显示的元素内容
        self.retranslateUi(Dialog)
        # 关联界面元素和槽函数
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # 填写各界面元素的内容
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton1.setText(_translate("Dialog", "登录"))
        self.pushButton_2.setText(_translate("Dialog", "退出"))
        self.label1.setText(_translate("Dialog", "欢迎使用本银行系统"))
        self.label.setText(_translate("Dialog", "账户名："))
        self.label_2.setText(_translate("Dialog", "密码："))


# 主函数，可以直接运行生成的界面
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
