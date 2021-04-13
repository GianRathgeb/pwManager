import functions
import hashlib
import fileHandlerClasses


class PasswordManager:
        def __init__(self):
                self.strFilePath = input("Enter file name (default: passwords.csv): ")
                if self.strFilePath == "":
                        self.strFilePath = "passwords.csv"
                self.strKey = input("Enter Password to encrypt passwords: ")
                self.menuFunctionsDict = {}
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

        def AddMenuFunction(self, number, function, arguments):
                self.menuFunctionsDict[number] = (function, arguments)

        def MenuHandler(self):
                print(self.menuFunctionsDict, self.intUserMenuChoice)
                menuChoise = self.intUserMenuChoice
                self.menuFunctionsDict[menuChoise][0](*self.menuFunctionsDict[menuChoise][1])
                        
