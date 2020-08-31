from forms.MenuForm import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MenuForm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setWindowIcon(QIcon('.//img//backgroung_image.jpg'))
    sys.exit(app.exec_())


