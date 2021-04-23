import time
import hashlib
from dictNumbers import numberDict

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def xor(a, b):
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

def fnStrToBin (StringToBin):
    arrCharsBin = []
    for char in [char for char in StringToBin]:
        if isInt(char):
            add = numberDict[int(char)].zfill(8)
            arrCharsBin.append(f"{add}")
        else:
            add  = bin(ord(char)).replace('0b', '').zfill(8)
            arrCharsBin.append(f"{add}")
    returnStr = ''
    for charBin in arrCharsBin:
        returnStr += charBin
    return returnStr

def fnEncryptString(strPassword, strKey):
    # Password String to binary string
    strBinaryPW = fnStrToBin(strPassword)

    # Key string to binary string
    strBinaryKey = fnStrToBin(strKey)
    # repeat key until every bit from pw can be xor'ed with the key
    strBinaryKey = (strBinaryKey * (int(len(strBinaryPW)/len(strBinaryKey))+1))[:len(strBinaryPW)]

    # Perform the binary xor operation
    strXor = xor(strBinaryPW, strBinaryKey)

    # Create the cipher text with the result of the binary xor
    strCipherText = ''
    for strcharcipherText in range(0, len(strXor), 8):
        strCipherText += str(int(strXor[strcharcipherText : strcharcipherText + 8], 2)).zfill(3)
    # return the cipher text
    return strCipherText


def fnDecryptString(strCiperText, strKey):
    # Ciphertext string to binary string
    strBinaryCipherText = ''
    for i in range(0, len(strCiperText), 3):
        strBinaryCipherText += f"{bin(int(strCiperText[i : i + 3]))}".replace("0b", "").zfill(8)

    # Key string to binary string
    strBinaryKey = fnStrToBin(strKey)
    # repeat key until there is a bit for every bit in the cipher text
    strBinaryKey = (strBinaryKey * (int(len(strBinaryCipherText)/len(strBinaryKey))+1))[:len(strBinaryCipherText)]


    # perform the xor operation
    binXorResult = xor(strBinaryCipherText, strBinaryKey)


    # create the clear text with the result of the binary xor
    strClearText = ''
    for index in range(0, len(binXorResult), 8):
        strClearText += chr(int(binXorResult[index : index + 8], 2))

    # return the clear text
    return strClearText

