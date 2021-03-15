import functions
import fileHandler

#print(functions.fnEncryptString('TestPassword', 'TestKey'))

strFilePath = input("Enter file name (default: passwords.csv): ")
if strFilePath == "":
        strFilePath = "passwords.csv"

strPassword = input("Enter Password to encrypt passwords: ")

test = fileHandler.fnReadPasswords(strFilePath)
for i in test:
    print(functions.fnDecryptString(i, strPassword))
