import functions
import fileHandler
import hashlib

#! Key to test: TestKey

def fnChooseMenu(strShowMenu, strShowError, **kwargs):
        
        try:
                intUserInput = int(input(strShowMenu))
                print("Select: " + kwargs["m" + str(intUserInput)])
                return intUserInput
        except ValueError:
                print(strShowError)
                fnChooseMenu(strShowMenu, strShowError)
        except KeyError:
                print(strShowError)
                fnChooseMenu(strShowMenu, strShowError)

def fnMenu(strPassword, strFilePath, arrPasswords, strHashPassword):
        menu = fnChooseMenu("1: Show all passwords\n2: Input new Password\n3: Delete a Password\n4: Exit Program\n", "Please a valid menu! ", m1="Show all passwords", m2 = "Input new Password", m3 = "Delete a Password", m4 = "Exit program")
        if menu == 1:
                print("\n\n")
                for i, j in enumerate(arrPasswords):
                        print(i, j[1])
                print("\n\n")
                fnReadPasswords(strFilePath, strPassword)
        elif menu == 2:
                print("\n\n")
                newPassword = input("Enter a new password:\n")
                newPassword = functions.fnEncryptString(newPassword, strPassword)
                fileHandler.fnWritePassword(strFilePath, newPassword)
                print("\n\n")   
                fnReadPasswords(strFilePath, strPassword)

        elif menu == 3:
                print("\n\n")
                for i, j in enumerate(arrPasswords):
                        print(i, j[1])
                deletePassword = int(input("Which password do you want to delete? (Use number)\n"))
                arrPasswords.pop(deletePassword)
                fileHandler.fnRewriteFile(strFilePath, strHashPassword, arrPasswords)
                print("\n\n")
                fnReadPasswords(strFilePath, strPassword)
        elif menu == 4:
                exit()

def fnInit():
        strFilePath = input("Enter file name (default: passwords.csv): ")
        if strFilePath == "":
                strFilePath = "passwords.csv"

        strPassword = input("Enter Password to encrypt passwords: ")
        print("\n\n\n\n\n\n\n\nPassword Manager by Gian Rathgeb\n\n")
        fnReadPasswords(strFilePath, strPassword)

def fnReadPasswords(strFilePath, strPassword):
        test = fileHandler.fnReadPasswords(strFilePath)
        arrPasswords = []
        for i, j in enumerate(test):
                if i > 0:
                        tempPassword = functions.fnDecryptString(j, strPassword)
                        arrPasswords.append([j, tempPassword])
                else:
                        strHashPassword = j
                        if not functions.fnValidateKey(strHashPassword, strPassword):
                                print("Wrong Password!")
                                exit(0)
        fnMenu(strPassword, strFilePath, arrPasswords, strHashPassword)



fnInit()

# TODO: Make the manager and file handler class based

