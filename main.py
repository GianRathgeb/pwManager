import functions
import hashlib
import fileHandlerClasses

#! Key to test: TestKey

def fnChooseMenu(strShowError, **kwargs):
        strShowMenu = ""
        for key, value in kwargs.items():
                strShowMenu += f"{key[-1]}: {value}\n"
        try:
                intUserInput = int(input(strShowMenu))
                print("Select: " + kwargs["m" + str(intUserInput)])
                return intUserInput
        except ValueError:
                print(strShowError)
                fnChooseMenu(strShowError, **kwargs)
        except KeyError:
                print(strShowError)
                fnChooseMenu(strShowError, **kwargs)


def fnMenu(arrPasswords):
        global fileWriter
        global strKey
        menu = fnChooseMenu("Please a valid menu! ", m1="Show all passwords", m2 = "Input new Password", m3 = "Delete a Password", m4 = "Exit program")
        if menu == 1:
                print("\n\n")
                for i, j in enumerate(arrPasswords):
                        print(i, j[1])
                print("\n\n")
                fnReadPasswords()
        elif menu == 2:
                print("\n\n")
                newPassword = input("Enter a new password:\n")
                newPassword = functions.fnEncryptString(newPassword, strKey)
                fileWriter.fnWritePassword(newPassword)
                print("\n\n")   
                fnReadPasswords()

        elif menu == 3:
                print("\n\n")
                for i, j in enumerate(arrPasswords):
                        print(i, j[1])
                deletePassword = int(input("Which password do you want to delete? (Use number)\n"))
                try:
                        arrPasswords.pop(deletePassword)
                        global keyHash
                        fileWriter.fnRewriteFile(arrPasswords)
                        print("\n\n")
                        fnReadPasswords()
                except IndexError:
                        print("Please enter a correct password")
                        fnReadPasswords()
        elif menu == 4:
                exit()


def fnReadPasswords():
        global strKey
        fileWriter.fnReadPasswords()
        fnMenu(fileWriter.tempArr)


def fnInit():
        strFilePath = input("Enter file name (default: passwords.csv): ")
        if strFilePath == "":
                strFilePath = "passwords.csv"
        global strKey
        strKey = input("Enter Password to encrypt passwords: ")
        global fileWriter
        fileWriter = fileHandlerClasses.FileWriter(strFilePath, strKey)
        print("\n\n\n\n\n\n\n\nPassword Manager by Gian Rathgeb\n\n")
        fnReadPasswords()


fileWriter = None
strKey = ""
keyHash = ""
fnInit()

# TODO: Make the manager should be class based