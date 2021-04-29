# Color picker: https://material.io/design/color/the-color-system.html#tools-for-picking-colors
# Color: #300079

from PyQt5 import *
from PyQt5.QtCore import *
from FirstVersion import *

from functions import *

if __name__ == "__main__":
    # Setup the UI
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Configure the UI
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ui.btn_close.clicked.connect(lambda: close_program(MainWindow))

    # Show the UI
    MainWindow.show()
    sys.exit(app.exec_())
