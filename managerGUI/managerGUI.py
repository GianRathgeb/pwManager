# Color picker: https://material.io/design/color/the-color-system.html#tools-for-picking-colors
# Color: #300079


from PyQt5 import *
from PyQt5.QtCore import *
from FirstVersion import *

from functions import *

# TODO: Implement a better resize function (which resizes everything)


if __name__ == "__main__":
    # Setup the UI
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Configure the UI
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ui.btn_close.clicked.connect(MainWindow.close)
    ui.btn_maximize_restore.clicked.connect(lambda: maximise_window(MainWindow))
    ui.btn_minimize.clicked.connect(MainWindow.showMinimized)

    # Show the UI
    MainWindow.show()
    sys.exit(app.exec_())
