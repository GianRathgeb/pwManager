from tableModel import TableModel
import time
import hashlib
from dictNumbers import numberDict
import csv
import hashlib


class Functions():
    def __init__(self, ui, fileName, strKey):
        # Init function, define variables
        self.ui = ui
        self.strFileName = fileName
        self.strKey = strKey
        self.keyValidated = False
        self.stateHasChanged = True



    def showPasswords(self):
        # show the passwords, read them from tempArr and create a table model
        if self.stateHasChanged:
            self.fnReadPasswords()
            tablePasswords = []
            if self.keyValidated:
                for i, pw in enumerate(self.tempArr):
                    temp = pw[1].split(";")
                    tablePasswords.append([i, temp[0], temp[1]])

                self.model = TableModel(tablePasswords)
                self.ui.table_view_your_passwords.setModel(self.model)
                self.ui.table_view_your_passwords.horizontalHeader().setStretchLastSection(True)
                self.stateHasChanged = False



    def isInt(self, s):
        # check if an inputted character is type = string
        try:
            int(s)
            return True
        except ValueError:
            return False

    def xor(self, a, b):
        # perform the bitwise x-or on the a and b binary string inputted
        ans = ""
        # Loop to iterate over the
        # Binary Strings
        for i in range(len(a)):
            # If the Character matches
            if (str(a[i]) == str(b[i])):
                ans += "0"
            else:
                ans += "1"
        return ans

    def fnStrToBin(self, StringToBin):
        # translate a string into a binary string
        arrCharsBin = []
        for char in [char for char in StringToBin]:
            if self.isInt(char):
                add = numberDict[int(char)].zfill(8)
                arrCharsBin.append(f"{add}")
            else:
                add = bin(ord(char)).replace('0b', '').zfill(8)
                arrCharsBin.append(f"{add}")
        returnStr = ''
        for charBin in arrCharsBin:
            returnStr += charBin
        return returnStr

    def fnEncryptString(self, strPassword, strKey):
        # Password String to binary string
        strBinaryPW = self.fnStrToBin(strPassword)

        # Key string to binary string
        strBinaryKey = self.fnStrToBin(strKey)
        # repeat key until every bit from pw can be xor'ed with the key
        try:
            strBinaryKey = (
                strBinaryKey * (int(len(strBinaryPW)/len(strBinaryKey))+1))[:len(strBinaryPW)]
        except ZeroDivisionError:
            # happens if no key give
            exit()
        # Perform the binary xor operation
        strXor = self.xor(strBinaryPW, strBinaryKey)

        # Create the cipher text with the result of the binary xor
        strCipherText = ''
        for strcharcipherText in range(0, len(strXor), 8):
            strCipherText += str(
                int(strXor[strcharcipherText: strcharcipherText + 8], 2)).zfill(3)
        # return the cipher text
        return strCipherText

    def fnDecryptString(self, strCiperText, strKey):
        # Ciphertext string to binary string
        strBinaryCipherText = ''
        for i in range(0, len(strCiperText), 3):
            strBinaryCipherText += f"{bin(int(strCiperText[i : i + 3]))}".replace(
                "0b", "").zfill(8)

        # Key string to binary string
        strBinaryKey = self.fnStrToBin(strKey)
        # repeat key until there is a bit for every bit in the cipher text
        try:
            strBinaryKey = (strBinaryKey * (int(len(strBinaryCipherText) /
                                                len(strBinaryKey))+1))[:len(strBinaryCipherText)]
        except ZeroDivisionError:
            # happens if no key give
            exit()

        # perform the xor operation
        binXorResult = self.xor(strBinaryCipherText, strBinaryKey)

        # create the clear text with the result of the binary xor
        strClearText = ''
        for index in range(0, len(binXorResult), 8):
            strClearText += chr(int(binXorResult[index: index + 8], 2))

        # return the clear text
        return strClearText


    def fnReadPasswords(self):
        # read all passwords from the password file (path required to create this object)
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
                tempPassword = self.fnDecryptString(j, self.strKey)
                self.tempArr.append([j, tempPassword])
            else:
                if not self.keyValidated:
                    self.keyHash = j
                    self.fnValidateKey()
                    if not self.keyValidated:
                        print("Wrong Key")

    def fnWritePassword(self, strPasswords):
        # write a new password to the end of the file
        with open(self.strFileName, mode='a+') as objPasswordFile:
            objPasswordFile.write(f"\n{strPasswords}")
        self.stateHasChanged = True

    def fnRewriteFile(self):
        # rewrite the complete password file (unly used when deleting a password)
        # only called by the fnDeletePassword function
        with open(self.strFileName, mode='w') as objPasswordFile:
            strToWrite = f"{self.keyHash}"
            for i in self.tempArr:
                strToWrite += f"\n{i[0]}"
            objPasswordFile.write(strToWrite)
        self.stateHasChanged = True

    def fnDeletePassword(self, set):
        # function that is called when you want to delete a password
        indexes = list(set)
        # Sort the list in reverse (no problems with indexes if multiple rows selected)
        indexes.sort(reverse=True)

        for i in range(0, len(indexes)):
            self.tempArr.pop(indexes[i])
        self.fnRewriteFile()

    def fnValidateKey(self):
        # compare the given key (while creating object) with the stored key in the file to validate it
        strKeyHash = hashlib.sha256(self.strKey.encode()).hexdigest()
        strHashToTest = self.fnEncryptString(strKeyHash, self.strKey)
        if self.keyHash == strHashToTest:
            self.keyValidated = True
        else:
            self.keyValidated = False

    def changeMaster(self, newKey):
        # change the master password
        strKeyHash = hashlib.sha256(newKey.encode()).hexdigest()
        strEncryptedHash = self.fnEncryptString(strKeyHash, newKey)
        newEncryptedPasswords = []
        # re-encrypt all passwords in the file
        for i, password in enumerate(self.tempArr):
            newEncryptedPasswords.append(
                [self.fnEncryptString(password[1], newKey), password[1]])
        # set all the variable and reprocess the file (write and read it again)
        self.tempArr = newEncryptedPasswords.copy()
        self.keyHash = strEncryptedHash
        self.strKey = newKey
        self.stateHasChanged = True
        self.fnRewriteFile()
        self.fnValidateKey()
        self.showPasswords()
