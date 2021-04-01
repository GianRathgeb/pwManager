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


def fnMenu(strPassword, arrPasswords):
        global fileWriter
        menu = fnChooseMenu("Please a valid menu! ", m1="Show all passwords", m2 = "Input new Password", m3 = "Delete a Password", m4 = "Exit program")
        if menu == 1:
                print("\n\n")
                for i, j in arrPasswords.items():
                        print(i, j[0])
                print("\n\n")
                fnReadPasswords(strPassword)
        elif menu == 2:
                print("\n\n")
                newPassword = input("Enter a new password:\n")
                newPassword = functions.fnEncryptString(newPassword, strPassword)
                fileWriter.fnWritePassword(newPassword)
                print("\n\n")   
                fnReadPasswords(strPassword)

        elif menu == 3:
                print("\n\n")
                for i, j in arrPasswords.items():
                        print(i, j[0])
                deletePassword = int(input("Which password do you want to delete? (Use number)\n"))
                try:
                        del arrPasswords[deletePassword]
                        global keyHash
                        fileWriter.fnRewriteFile(keyHash, arrPasswords)
                        print("\n\n")
                        fnReadPasswords(strPassword)
                except KeyError:
                        print("Please enter a correct password")
                        fnReadPasswords(strPassword)
        elif menu == 4:
                exit()


def fnReadPasswords(strPassword):
        fileWriter.fnReadPasswords()
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


def fnInit():
        strFilePath = input("Enter file name (default: passwords.csv): ")
        if strFilePath == "":
                strFilePath = "passwords.csv"
        global fileWriter
        fileWriter = fileHandlerClasses.FileWriter(strFilePath)
        global strKey
        strKey = input("Enter Password to encrypt passwords: ")
        print("\n\n\n\n\n\n\n\nPassword Manager by Gian Rathgeb\n\n")
        fnReadPasswords(strKey)


# Define global variables
fileWriter = None
strKey = ""
keyHash = ""
fnInit()

# TODO: Make the manager and file handler class based
# TODO: arrTemp should not be an array, it should be a dictionary