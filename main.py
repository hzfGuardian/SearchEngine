#!/usr/bin/env python
# coding=utf-8

from search import *
import PyQt5
if __name__ == "__main__":
        import sys    
        app = PyQt5.QtWidgets.QApplication(sys.argv)
        formObj = PyQt5.QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
        ui = Ui_MainWindow()
        ui.setupUi(formObj)
        formObj.show()
        sys.exit(app.exec_())
