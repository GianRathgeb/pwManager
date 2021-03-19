import functions
import fileHandler

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
for i, j in enumerate(test):
        if i > 0:
                print(functions.fnDecryptString(j, strPassword))
        else:
                functions.fnValidateKey(j, strPassword)


menu = fnChooseMenu("1: Input new PW\n2: Exit Program\n", "Please a valid menu! ", m1 = "Input new PW", m2 = "Exit program")

if menu == 1:
        newPassword = input("Enter a new password:\n")
        newPassword = functions.fnEncryptString(newPassword, strPassword)
        fileHandler.fnWritePassword(strFilePath, [newPassword])

elif menu == 2:
        exit()
