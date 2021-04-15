from passwordManagerClass import PasswordManager
from fileHandlerClasses import FileWriter
import functions
import menuFunctions as mF

#! Key to test: TestKey


# Initialize the password manager
PasswordManager = PasswordManager()

# Initialize the fileWriter
fileWriter = FileWriter(PasswordManager.strFilePath, PasswordManager.strKey)
# Read all passwords to file writer
fileWriter.fnReadPasswords()

# Add the file writer to the password manager (only reference) so that the password manager can work with the file writer
PasswordManager.AddFileWriter(fileWriter)


# Add the menu to the password manager
PasswordManager.CreateMenu("Please a valid menu! ", m1="Show all passwords",
                           m2="Input new Password", m3="Delete a Password", m4="Exit program")
PasswordManager.AddMenuFunction(1, mF.fnMenu1, (fileWriter.tempArr))
PasswordManager.AddMenuFunction(2, mF.fnMenu2, (PasswordManager.strKey, fileWriter.fnWritePassword))
PasswordManager.AddMenuFunction(3, mF.fnMenu3, (fileWriter.tempArr, fileWriter.fnRewriteFile))
PasswordManager.AddMenuFunction(4, mF.fnMenu4, ())

# loop to print the menu
while True:
    PasswordManager.PrintMenu()
    PasswordManager.MenuHandler()
    fileWriter.fnReadPasswords()


# TODO: Errors in the read and delete function, possible solution: accept parameters in menu functions as *args
