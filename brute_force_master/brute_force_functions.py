# Functions used by the brute forcer
# all of the functions are copied from the functions.py file in the main branch
# but they are modified since this program is not object oriented


# this is just a const of the number dict file:
numberDict = {
    0: "0110000",
    1: "0110001",
    2: "0110010",
    3: "0110011",
    4: "0110100",
    5: "0110101",
    6: "0110110",
    7: "0110111",
    8: "0111000",
    9: "0111001"
}

# this is just the xor function of the original program
def xor(a, b):
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
    
# this is the isInt function of the original program
def isInt(s):
    # check if an inputted character is type = string
    try:
        int(s)
        return True
    except ValueError:
        return False
    
# this is the string to binary function of the original program
def fnStrToBin(StringToBin):
    # translate a string into a binary string
    arrCharsBin = []
    for char in [char for char in StringToBin]:
        if isInt(char):
            add = numberDict[int(char)].zfill(8)
            arrCharsBin.append(f"{add}")
        else:
            add = bin(ord(char)).replace('0b', '').zfill(8)
            arrCharsBin.append(f"{add}")
    returnStr = ''
    for charBin in arrCharsBin:
        returnStr += charBin
    return returnStr

# this is the encryption function of the original program
def fnEncryptString(strPassword, strKey):
    # Password String to binary string
    strBinaryPW = fnStrToBin(strPassword)

    # Key string to binary string
    strBinaryKey = fnStrToBin(strKey)
    # repeat key until every bit from pw can be xor'ed with the key
    try:
        strBinaryKey = (
            strBinaryKey * (int(len(strBinaryPW)/len(strBinaryKey))+1))[:len(strBinaryPW)]
    except ZeroDivisionError:
        # happens if no key give
        exit()
    # Perform the binary xor operation
    strXor = xor(strBinaryPW, strBinaryKey)

    # Create the cipher text with the result of the binary xor
    strCipherText = ''
    for strcharcipherText in range(0, len(strXor), 8):
        strCipherText += str(
            int(strXor[strcharcipherText: strcharcipherText + 8], 2)).zfill(3)
    # return the cipher text
    return strCipherText

