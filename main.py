#!/usr/bin/env python
# coding=utf-8

from search import *

if __name__=="__main__":
        import sys    
        app = QtWidgets.QApplication(sys.argv)    
        formObj = QtWidgets.QMainWindow()  #注意，这里和我们一开始创建窗体时使用的界面类型相同  
        ui = Ui_MainWindow()
        ui.setupUi(formObj)
        formObj.show()
        sys.exit(app.exec_())
