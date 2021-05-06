import functio
import hashlib
import fileHandlerClasses



class PasswordManager:
        def __init__(self):
                self.strFilePath = input("Enter file name (default: passwords.csv): ")
                if self.strFilePath == "":
                        self.strFilePath = "passwords.csv"
                self.strKey = input("Enter Password to encrypt passwords: ")
                self.menufunctioDict = {}
                print("\n\n\n\n\n\n\n\nPassword Manager by Gian Rathgeb\n\n")


        def CreateMenu(self, error, **menu):
                self.menuError = error
                self.menuDict = menu


        def UpdateFileHandler(self, fileHandler):
                self.fileHandler = fileHandler


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

        def AddMenuFunction(self, number, function, arguments):
                self.menufunctioDict[number] = (function, arguments)

        def MenuHandler(self):
                menuChoice = self.intUserMenuChoice
                function = self.menufunctioDict[menuChoice][0]
                arguments = [*self.menufunctioDict[menuChoice][1]]
                function(*arguments)

                        