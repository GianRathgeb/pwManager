# Credit to Wanderson Magalhaes
# https://github.com/Wanderson-Magalhaes/Simple_PySide_Base


# Import modules
from managerModules import *
from tableModel import TableModel

# TODO: 
# * Function to delete selected password in the gui
# * Function to change the master password


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        UIFunctions.removeTitleBar(True)
        self.setWindowTitle('Password Manager - Gian Rathgeb')
        UIFunctions.labelTitle(self, 'Password Manager - Gian Rathgeb')
        UIFunctions.labelDescription(self, '')

        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)

        self.ui.btn_toggle_menu.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 220, True))
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home",
                               "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Add Password", "btn_new_password",
                               "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Custom Widgets", "btn_widgets",
                               "url(:/16x16/icons/16x16/cil-settings.png)", False)

        UIFunctions.selectStandardMenu(self, "btn_home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        self.ui.btn_password_add.clicked.connect(self.addPassword)
        self.ui.btn_password_abort.clicked.connect(self.clearPassword)

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        UIFunctions.uiDefinitions(self)
        self.show()

    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))
            self.functionsObject.showPasswords()

        # PAGE NEW PASSWORD
        if btnWidget.objectName() == "btn_new_password":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_add_password)
            UIFunctions.resetStyle(self, "btn_new_password")
            UIFunctions.labelPage(self, "New Password")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "Custom Widgets")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))

    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')

    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) +
              ' | Text Press: ' + str(event.text()))

    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) +
              ' | Width: ' + str(self.width()))

    def addFunctionsObject(self, fnObject):
        self.functionsObject = fnObject

    def addPassword(self):
        strPassword = str(self.ui.txt_password.text()).replace(';', '')
        strPasswordName = str(self.ui.txt_password_name.text()).replace(';', '')
        strEncryptedPassword = self.functionsObject.fnEncryptString(
            f"{strPasswordName};{strPassword}", self.functionsObject.strKey)
        self.functionsObject.fnWritePassword(strEncryptedPassword)
        self.ui.txt_password.setText("")
        self.ui.txt_password_name.setText("")

    def clearPassword(self):
        self.ui.txt_password.setText("")
        self.ui.txt_password_name.setText("")


# Init password manager
if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    # TODO: Functions to input the key
    functions = Functions(window.ui, "passwords.csv", "TestKey")
    window.addFunctionsObject(functions)
    functions.showPasswords()
    sys.exit(app.exec_())
