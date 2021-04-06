import functions
import hashlib
import fileHandlerClasses

#! Key to test: TestKey

class PasswordManager:
        def __init__(self):
                self.strFilePath = input("Enter file name (default: passwords.csv): ")
                if self.strFilePath == "":
                        self.strFilePath = "passwords.csv"
                self.strKey = input("Enter Password to encrypt passwords: ")
                print("\n\n\n\n\n\n\n\nPassword Manager by Gian Rathgeb\n\n")


        def addFileWriter(self, fileWriter):
                self.referenceFileWriter = fileWriter


        def fnPrintMenu(self, strShowError, **dictMenuItems):
                strShowMenu = ""
                for key, value in dictMenuItems.items():
                        strShowMenu += f"{key[-1]}: {value}\n"
                try:
                        intUserInput = int(input(strShowMenu))
                        print("Select: " + dictMenuItems["m" + str(intUserInput)])
                        return intUserInput
                except ValueError:
                        print(strShowError)
                        self.fnPrintMenu(strShowError, **dictMenuItems)
                except KeyError:
                        print(strShowError)
                        self.fnPrintMenu(strShowError, **dictMenuItems)


        def fnMenu(self):
                self.referenceFileWriter.fnReadPasswords()
                menu = self.fnPrintMenu("Please a valid menu! ", m1="Show all passwords", m2 = "Input new Password", m3 = "Delete a Password", m4 = "Exit program")
                if menu == 1:
                        print("\n\n")
                        for i, j in enumerate(fileWriter.tempArr):
                                print(i, j[1])
                        print("\n\n")
                elif menu == 2:
                        print("\n\n")
                        newPassword = input("Enter a new password:\n")
                        newPassword = functions.fnEncryptString(newPassword, self.strKey)
                        fileWriter.fnWritePassword(newPassword)
                        print("\n\n")   

                elif menu == 3:
                        print("\n\n")
                        for i, j in enumerate(fileWriter.tempArr):
                                print(i, j[1])
                        deletePassword = int(input("Which password do you want to delete? (Use number)\n"))
                        try:
                                fileWriter.tempArr.pop(deletePassword)
                                fileWriter.fnRewriteFile(fileWriter.tempArr)
                                print("\n\n")
                        except IndexError:
                                print("Please enter a correct password")
                elif menu == 4:
                        exit()



        


# Initialize the password manager
PasswordManager = PasswordManager()
# Initialize the fileWriter
fileWriter = fileHandlerClasses.FileWriter(PasswordManager.strFilePath, PasswordManager.strKey)
# Add the file writer to the password manager (only reference) so that the password manager can work with the file writer
PasswordManager.addFileWriter(fileWriter)

# loop to print the menu
while True:
        PasswordManager.fnMenu()
