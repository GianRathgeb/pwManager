import functions
import fileHandler
import hashlib

# TODO: Use object for password manager and file handler

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

strFilePath = input("Enter file name (default: passwords.csv): ")
if strFilePath == "":
        strFilePath = "passwords.csv"

strPassword = input("Enter Password to encrypt passwords: ")

test = fileHandler.fnReadPasswords(strFilePath)
arrPasswords = []
for i, j in enumerate(test):
        if i > 0:
                tempPassword = functions.fnDecryptString(j, strPassword)
                arrPasswords.append([j, tempPassword])
                print(tempPassword)
        else:
                strHashPassword = j
                if not functions.fnValidateKey(strHashPassword, strPassword):
                        print("Wrong Password!")
                        exit(0)


menu = fnChooseMenu("1: Input new Password\n2: Delete a Password\n3: Exit Program\n", "Please a valid menu! ", m1 = "Input new Password", m2= "Delete a Password", m3 = "Exit program")

if menu == 1:
        newPassword = input("Enter a new password:\n")
        newPassword = functions.fnEncryptString(newPassword, strPassword)
        fileHandler.fnWritePassword(strFilePath, newPassword)
elif menu == 2:
        for i, j in enumerate(arrPasswords):
                print(i, j[1])
        deletePassword = int(input("Which password do you want to delete? (Use number)\n"))
        arrPasswords.pop(deletePassword)
        fileHandler.fnRewriteFile(strFilePath, strHashPassword, arrPasswords)
elif menu == 3:
        exit()
