import time

def fnEncryptString(strPassword, strKey):
    # Password String to binary string
    strBinaryPW = ''
    for char in [bin(ord(char)) for char in strPassword]:
        strBinaryPW += char.replace('0b', '')
    # Key string to binary string
    strBinaryKey = ''
    for char in [bin(ord(char)) for char in strKey]:
        strBinaryKey += char.replace('0b', '')
    # repeat key until every bit from pw can be xor'ed with the key
    strBinaryKey = (strBinaryKey * (int(len(strBinaryPW)/len(strBinaryKey))+1))[:len(strBinaryPW)]

    # Perform the binary xor operation
    binBinaryXor = int(strBinaryPW,2) ^ int(strBinaryKey,2)
    # Cut the '0b' of the beginning and add missing 0 at the beginning
    strXor = '0' + bin(binBinaryXor)[2:]

    # fill the beginning with zeros so there are 7 binary numbers in the first char
    strXor = strXor.zfill(len(strBinaryPW))

    # Create the cipher text with the result of the binary xor
    strCipherText = ''
    for strcharcipherText in range(0, len(strXor), 7):
        strCipherText += str(int(strXor[strcharcipherText : strcharcipherText + 7], 2)).zfill(3)
    # return the cipher text
    return strCipherText


def fnDecryptString(strCiperText, strKey):
    # Ciphertext string to binary string
    strBinaryCipherText = ''
    for i in range(0, len(strCiperText), 3):
        #! Sometime this if is needed, sometimes not
        #if i < len(strCiperText) - 3:
        strBinaryCipherText += bin(int(strCiperText[i : i + 3])).replace("0b", "").zfill(7)
        #else:
        #    strBinaryCipherText += bin(int(strCiperText[i : i + 3])).replace("0b", "").zfill(6)

    # Key string to binary string
    strBinaryKey = ''
    for strBinaryCharKey in [bin(ord(char)) for char in strKey]:
        strBinaryKey += strBinaryCharKey.replace('0b', '')
    # repeat key until there is a bit for every bit in the cipher text
    strBinaryKey = (strBinaryKey * (int(len(strBinaryCipherText)/len(strBinaryKey))+1))[:len(strBinaryCipherText)]


    # perform the xor operation
    strBinaryXor = int(strBinaryCipherText,2) ^ int(strBinaryKey,2)
    # Cut of the '0b' at the beginning
    binXorResult = bin(strBinaryXor)[2:]


    # create the clear text with the result of the binary xor
    strClearText = ''
    for index in range(0, len(binXorResult), 7):
        strClearText += chr(int(binXorResult[index : index + 7], 2))

    # return the clear text
    return strClearText

