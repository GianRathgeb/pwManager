# Credit to Wanderson Magalhaes, the GUI is inspired by him
# https://github.com/Wanderson-Magalhaes/Simple_PySide_Base
# The rest of the code and GUI was made by Gian Rathgeb
# https://github.com/gianrathgeb
# https://linkedin.com/in/gianrathgeb


# Version: 0.5


# Import modules
from PySide2.QtCore import QAbstractTableModel
from managerModules import *


# TODO: 
# * List view makes window blinking when resizing (still no solution for this problem)
# * Clean code

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

        # DEFINE BUTTON ACTIONS
        self.ui.lbl_wrong_password.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_startup)
        self.ui.btn_password_add.clicked.connect(self.addPassword)
        self.ui.btn_password_abort.clicked.connect(self.clearPassword)
        self.ui.btn_delete_pasword.clicked.connect(self.deletePassword)
        self.ui.btn_submit_master.clicked.connect(self.submitMaster)
        self.ui.btn_cancel_master.clicked.connect(lambda: sys.exit())
        self.ui.btn_apply_new_settings.clicked.connect(self.applySettings)

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
        # First check if the key is validated (used to prevent unauthorized access)
        if self.functionsObject.keyValidated:
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
                # When the button is pressed, set to focus to the text field
                self.ui.txt_password_name.setFocus()

            # PAGE SETTINGS
            if btnWidget.objectName() == "btn_settings":
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
                UIFunctions.resetStyle(self, "btn_settings")
                UIFunctions.labelPage(self, "Settings")
                btnWidget.setStyleSheet(
                    UIFunctions.selectMenu(btnWidget.styleSheet()))
                self.ui.txt_current_master.setFocus()

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

    def addPassword(self):
        # Add a new password to the database
        strPassword = str(self.ui.txt_password.text()).replace(';', '')
        strPasswordName = str(self.ui.txt_password_name.text()).replace(';', '')
        strEncryptedPassword = self.functionsObject.fnEncryptString(
            f"{strPasswordName};{strPassword}", self.functionsObject.strKey)
        self.functionsObject.fnWritePassword(strEncryptedPassword)
        self.ui.txt_password.setText("")
        self.ui.txt_password_name.setText("")

    def clearPassword(self):
        # Clear input fields of the add password menu
        self.ui.txt_password.setText("")
        self.ui.txt_password_name.setText("")

    def deletePassword(self):
        # Delete a password from the database
        indexes = self.ui.table_view_your_passwords.selectedIndexes()
        rows = set()
        for index in indexes:
            rows.add(index.row())
        self.functionsObject.fnDeletePassword(rows)
        self.functionsObject.showPasswords()

    def applySettings(self):
        # change settings, will be executed when pressing the apply button in the settings page
        inputCurrentKey = self.ui.txt_current_master.text()
        if self.functionsObject.strKey == inputCurrentKey:
            # when the current key is correct
            newKey = self.ui.txt_new_master_password.text()
            confirmKey = self.ui.txt_confirm_new_master.text()
            if newKey == confirmKey:
                # when the new key is correctly typed in 2 times
                self.functionsObject.changeMaster(newKey)
                self.ui.txt_new_master_password.setText('')
                self.ui.txt_confirm_new_master.setText('')
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        else:
            # when the current key is not correct
            print("Wrong Master Passwords entered")

    def submitMaster(self):
        # validate master password, only executed when master password needs to be inputted
        masterKey = self.ui.txt_master_password.text()
        filename = self.ui.txt_password_file.text()
        # Next if needed, else the program would close if no key entered
        if masterKey == "":
            masterKey = "™" # You cannot type this character, so this key will not be valid
        if filename == "":
            filename = "passwords.csv"
        self.functionsObject = Functions(self.ui, filename, masterKey)
        self.functionsObject.showPasswords()
        if self.functionsObject.keyValidated:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.functionsObject.showPasswords()
            UIFunctions.addNewMenu(self, "HOME", "btn_home",
                               "url(:/16x16/icons/16x16/cil-home.png)", True)
            UIFunctions.addNewMenu(self, "Add Password", "btn_new_password",
                                "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
            UIFunctions.addNewMenu(self, "Settings", "btn_settings",
                                "url(:/16x16/icons/16x16/cil-settings.png)", False)
            UIFunctions.selectStandardMenu(self, "btn_home")
        else:
            self.ui.lbl_wrong_password.show()


# Init password manager
if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segseui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
