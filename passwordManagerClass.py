import functions
import hashlib
import fileHandlerClasses


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
                        self.intUserMenuChoice = int(input(strShowMenu))
                        print("Select: " + self.menuDict["m" + str(self.intUserMenuChoice)])
                except:
                        print(self.menuError)
                        self.PrintMenu()


        def MenuHandler(self):
                self.referenceFileWriter.fnReadPasswords()
                if self.intUserMenuChoice == 1:
                        print("\n\n")
                        for i, j in enumerate(self.referenceFileWriter.tempArr):
                                print(i, j[1])
                        print("\n\n")
                elif self.intUserMenuChoice == 2:
                        print("\n\n")
                        newPassword = input("Enter a new password:\n")
                        newPassword = functions.fnEncryptString(newPassword, self.strKey)
                        self.referenceFileWriter.fnWritePassword(newPassword)
                        print("\n\n")   

                elif self.intUserMenuChoice == 3:
                        print("\n\n")
                        for i, j in enumerate(self.referenceFileWriter.tempArr):
                                print(i, j[1])
                        deletePassword = int(input("Which password do you want to delete? (Use number)\n"))
                        try:
                                self.referenceFileWriter.tempArr.pop(deletePassword)
                                self.referenceFileWriter.fnRewriteFile(self.referenceFileWriter.tempArr)
                                print("\n\n")
                        except IndexError:
                                print("Please enter a correct password")
                elif self.intUserMenuChoice == 4:
                        exit()
