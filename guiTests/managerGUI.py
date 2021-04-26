from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from FirstVerion import Ui_MainWindow


if __name__ == "__main__":
    # Setup the UI
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Configure the UI
    MainWindow.setWindowFlag(Qt.FramelessWindowHint)
    ui.btnClose.clicked.connect(sys.exit)

    # Show the UI
    MainWindow.show()
    sys.exit(app.exec_())
