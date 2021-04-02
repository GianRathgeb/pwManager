import csv
import hashlib
import functions

class FileWriter:
    def __init__(self, fileName, strKey):
        self.strFileName = fileName
        self.strKey = strKey


    def fnReadPasswords(self):
        with open(self.strFileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            self.arrPasswords = []
            for row in csv_reader:
                try:
                    self.arrPasswords.append(row[0])
                except IndexError:
                    print("No Passwords found in file")
<<<<<<< HEAD
        self.tempArr = []
        for i, j in enumerate(self.arrPasswords):
                if i > 0:
                        tempPassword = functions.fnDecryptString(j, self.strKey)
                        self.tempArr.append([j, tempPassword])
                else:
                        self.keyHash = j
                        if not self.fnValidateKey(self.keyHash, self.strKey):
                                exit(0)
=======

>>>>>>> 2a601af386dcd95ec983f015803d053df856d26f
        

    def fnWritePassword(self, strPassword):
        with open(self.strFileName, mode='a+') as objPasswordFile:
            objPasswordFile.write(f"\n{strPassword}")

<<<<<<< HEAD
    def fnRewriteFile(self, arrPasswords):
        with open(self.strFileName, mode='w') as objPasswordFile:
            strToWrite = f"{self.keyHash}"
            for i in arrPasswords:
                strToWrite += f"\n{i[0]}"
=======

    def fnRewriteFile(self, strPasswordHash, dictPassword):
        with open(self.strFileName, mode='w') as objPasswordFile:
            strToWrite = f"{strPasswordHash}"
            for password in dictPassword.items():
                strToWrite += f"\n{password[1][1]}"
>>>>>>> 2a601af386dcd95ec983f015803d053df856d26f
            objPasswordFile.write(strToWrite)


    def fnValidateKey(self, encrpytedHash, key):
        strKeyHash = hashlib.sha256(key.encode()).hexdigest()
        strHashToTest = functions.fnEncryptString(strKeyHash, key)
        if encrpytedHash == strHashToTest:
            return True
        else: 
            return False
