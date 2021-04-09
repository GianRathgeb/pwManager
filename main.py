import functions
import hashlib
import fileHandlerClasses

#! Key to test: TestKey


def fnPrintMenu(strShowError, **dictMenuItems):
        strShowMenu = ""
        for key, value in dictMenuItems.items():
                strShowMenu += f"{key[-1]}: {value}\n"
        try:
                intUserInput = int(input(strShowMenu))
                print("Select: " + dictMenuItems["m" + str(intUserInput)])
                return intUserInput
        except ValueError:
                print(strShowError)
                fnPrintMenu(strShowError, **dictMenuItems)
        except KeyError:
                print(strShowError)
                fnPrintMenu(strShowError, **dictMenuItems)


def fnMenu():
        global fileWriter
        fileWriter.fnReadPasswords()
        global strKey
        menu = fnPrintMenu("Please a valid menu! ", m1="Show all passwords", m2 = "Input new Password", m3 = "Delete a Password", m4 = "Exit program")
        if menu == 1:
                print("\n\n")
                for i, j in enumerate(fileWriter.tempArr):
                        print(i, j[1])
                print("\n\n")
                fnMenu()
        elif menu == 2:
                print("\n\n")
                newPassword = input("Enter a new password:\n")
                newPassword = functions.fnEncryptString(newPassword, strKey)
                fileWriter.fnWritePassword(newPassword)
                print("\n\n")   
                fnMenu()

        elif menu == 3:
                print("\n\n")
                for i, j in enumerate(fileWriter.tempArr):
                        print(i, j[1])
                deletePassword = int(input("Which password do you want to delete? (Use number)\n"))
                try:
                        fileWriter.tempArr.pop(deletePassword)
                        global keyHash
                        fileWriter.fnRewriteFile(fileWriter.tempArr)
                        print("\n\n")
                        fnMenu()
                except IndexError:
                        print("Please enter a correct password")
                        fnMenu()
                        
        elif menu == 4:
                exit()


def fnInit():
        strFilePath = input("Enter file name (default: passwords.csv): ")
        if strFilePath == "":
                strFilePath = "passwords.csv"
        global strKey
        strKey = input("Enter Password to encrypt passwords: ")
        global fileWriter
        fileWriter = fileHandlerClasses.FileWriter(strFilePath, strKey)
        print("\n\n\n\n\n\n\n\nPassword Manager by Gian Rathgeb\n\n")
        fnMenu()


fileWriter = None
strKey = ""
keyHash = ""
fnInit()

# TODO: Make the manager should be class based