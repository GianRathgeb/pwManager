import functions
import hashlib
import fileHandlerClasses

#! Key to test: TestKey

class PasswordManager:
        def __init__(self):
                self.strFilePath = input("Enter file name (default: passwords.csv): ")
                if self.strFilePath == "":
                        self.strFilePath = "passwords.csv"
                self.strKey = input("Enter Password to encrypt passwords: ")
                print("\n\n\n\n\n\n\n\nPassword Manager by Gian Rathgeb\n\n")


        def CreateMenu(self, error, **menu):
                self.menuError = error
                self.menuDict = menu


        def AddFileWriter(self, fileWriter):
                self.referenceFileWriter = fileWriter


        def PrintMenu(self):
                strShowMenu = ""
                for key, value in self.menuDict.items():
                        strShowMenu += f"{key[-1]}: {value}\n"
                try:
                        intUserInput = int(input(strShowMenu))
                        print("Select: " + self.menuDict["m" + str(intUserInput)])
                        return intUserInput
                except (ValueError, KeyError) as exception:
                        print(self.menuError)
                        self.PrintMenu()


        def MenuHandler(self):
                self.referenceFileWriter.fnReadPasswords()
                menu = self.PrintMenu()
                if menu == 1:
                        print("\n\n")
                        for i, j in enumerate(fileWriter.tempArr):
                                print(i, j[1])
                        print("\n\n")
                elif menu == 2:
                        print("\n\n")
                        newPassword = input("Enter a new password:\n")
                        newPassword = functions.fnEncryptString(newPassword, self.strKey)
                        self.referenceFileWriter.fnWritePassword(newPassword)
                        print("\n\n")   

                elif menu == 3:
                        print("\n\n")
                        for i, j in enumerate(fileWriter.tempArr):
                                print(i, j[1])
                        deletePassword = int(input("Which password do you want to delete? (Use number)\n"))
                        try:
                                self.referenceFileWriter.tempArr.pop(deletePassword)
                                self.referenceFileWriter.fnRewriteFile(fileWriter.tempArr)
                                print("\n\n")
                        except IndexError:
                                print("Please enter a correct password")
                elif menu == 4:
                        exit()



        
# Initialize the password manager
PasswordManager = PasswordManager()

PasswordManager.CreateMenu("Please a valid menu! ", m1="Show all passwords", m2 = "Input new Password", m3 = "Delete a Password", m4 = "Exit program")
# Initialize the fileWriter
fileWriter = fileHandlerClasses.FileWriter(PasswordManager.strFilePath, PasswordManager.strKey)
# Add the file writer to the password manager (only reference) so that the password manager can work with the file writer
PasswordManager.AddFileWriter(fileWriter)

# loop to print the menu
while True:
        PasswordManager.MenuHandler()
