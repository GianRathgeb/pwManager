from PyQt5 import *
from PyQt5.QtCore import *
from FirstVersion import *


if __name__ == "__main__":
    # Setup the UI
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Configure the UI


    # Show the UI
    MainWindow.show()
    sys.exit(app.exec_())
