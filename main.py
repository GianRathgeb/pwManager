from passwordManagerClass import PasswordManager
from fileHandlerClasses import FileWriter

#! Key to test: TestKey

        
# Initialize the password manager
PasswordManager = PasswordManager()

PasswordManager.CreateMenu("Please a valid menu! ", m1="Show all passwords", m2 = "Input new Password", m3 = "Delete a Password", m4 = "Exit program")
# Initialize the fileWriter
fileWriter = FileWriter(PasswordManager.strFilePath, PasswordManager.strKey)
# Add the file writer to the password manager (only reference) so that the password manager can work with the file writer
PasswordManager.AddFileWriter(fileWriter)

# loop to print the menu
while True:
        PasswordManager.PrintMenu()
        PasswordManager.MenuHandler()

# TODO: Add modular menu (menu not defined password manager class), could add menu like create menu