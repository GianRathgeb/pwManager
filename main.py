import functions
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
                for i, j in arrPasswords.items():
                        print(i, j[0])
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
                for i, j in arrPasswords.items():
                        print(i, j[0])
                deletePassword = int(input("Which password do you want to delete? (Use number)\n"))
                try:
                        del arrPasswords[deletePassword]
                        global keyHash
                        fileWriter.fnRewriteFile(arrPasswords)
                        print("\n\n")
<<<<<<< HEAD
                        fnReadPasswords()
                except IndexError:
=======
                        fnReadPasswords(strPassword)
                except KeyError:
>>>>>>> 2a601af386dcd95ec983f015803d053df856d26f
                        print("Please enter a correct password")
                        fnReadPasswords()
        elif menu == 4:
                exit()


def fnReadPasswords():
        global strKey
        fileWriter.fnReadPasswords()
<<<<<<< HEAD
        fnMenu(fileWriter.tempArr)
=======
        dictPassword = {}
        for i, j in enumerate(fileWriter.arrPasswords):
                if i > 0:
                        tempPassword = functions.fnDecryptString(j, strPassword)
                        dictPassword[i - 1] = [tempPassword, j]
                else:
                        global strKey
                        global keyHash
                        keyHash = j
                        if not fileWriter.fnValidateKey(keyHash, strKey):
                                exit(0)
        fnMenu(strPassword, dictPassword)
>>>>>>> 2a601af386dcd95ec983f015803d053df856d26f


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


# Define global variables
fileWriter = None
strKey = ""
keyHash = ""
fnInit()

# TODO: Make the manager should be class based