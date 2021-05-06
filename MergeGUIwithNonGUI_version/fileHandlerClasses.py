import csv
import hashlib
import functio


class FileWriter:
    def __init__(self, fileName, strKey):
        self.strFileName = fileName
        self.strKey = strKey
        self.kayValidated = False

    def fnReadPasswords(self):
        with open(self.strFileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            self.arrPasswords = []
            for row in csv_reader:
                try:
                    self.arrPasswords.append(row[0])
                except IndexError:
                    print("No Passwords found in file")
        self.tempArr = []
        for i, j in enumerate(self.arrPasswords):
            if i >= 1:
                tempPassword = functio.fnDecryptString(j, self.strKey)
                self.tempArr.append([j, tempPassword])
            else:
                if not self.kayValidated:
                    self.keyHash = j
                    if not self.fnValidateKey(self.keyHash, self.strKey):
                        exit(0)

    def fnWritePassword(self, arrPasswords):
        with open(self.strFileName, mode='a+') as objPasswordFile:
            for password in arrPasswords:
                objPasswordFile.write(f"\n{password}")

    def fnRewriteFile(self):
        with open(self.strFileName, mode='w') as objPasswordFile:
            strToWrite = f"{self.keyHash}"
            for i in self.tempArr:
                strToWrite += f"\n{i[0]}"
            objPasswordFile.write(strToWrite)

    def fnValidateKey(self, encrpytedHash, key):
        strKeyHash = hashlib.sha256(key.encode()).hexdigest()
        strHashToTest = functio.fnEncryptString(strKeyHash, key)
        if encrpytedHash == strHashToTest:
            self.kayValidated = True
            return True
        else:
            return False
