import sys
from PyQt5 import QtWidgets
from myUiFile import myMainfile
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    desktop = QtWidgets.QApplication.desktop()
    screenRect = desktop.screenGeometry()
    height = screenRect.height()#显示器高度
    width = screenRect.width()#显示器长度
    ex = myMainfile()
    w = QtWidgets.QMainWindow()
    w.setMinimumSize(width/4,height/4)
    w.setMaximumSize(width/4,height/4)
    ex.setupUi(w)
    w.show()



    sys.exit(app.exec_())