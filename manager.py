

pw = "DE"
key = "C"


def encrypt(pw, key):
    binaryPW = [bin(ord(char)) for char in pw]
    test = ''
    for char in binaryPW:
        test += char.replace('0b', '')

    binaryPW =  test
    print('binary PW ' + binaryPW)

    binaryKey = [bin(ord(char)) for char in key]
    test = ''
    for char in binaryKey:
        test += char.replace('0b', '')

    # repeat key until 
    binaryKey = (test * (int(len(binaryPW)/len(test))+1))[:len(binaryPW)]

    print("bin key 1 " + binaryKey)

    test= int(binaryPW,2) ^ int(binaryKey,2)
    xor = bin(test)[2:]
    xor = xor.zfill(len(binaryPW))

    print("xor " + xor)

    result = []
    for index in range(0, len(xor), 7):
        result.append(xor[index : index + 7])

    test = ''
    for i in result:
        test  += str(int(i, 2)).zfill(3)

    print('test encrypt ' + test)
    return(test)


def decrypt(string, key):
    print('string ' + string)
    test = []
    for index in range(0, len(string), 3):
        test.append(bin(int(string[index : index + 3])).replace("0b", "")) 
    test1 = ""
    for i in test:
        test1 += i.zfill(7)
    print("test1 " + test1)

    binaryKey = [bin(ord(char)) for char in key]
    test = ''
    for char in binaryKey:
        test += char.replace('0b', '')

    # repeat key until 
    binaryKey = (test * (int(len(test1)/len(test1))+1))[:len(test1)]
    print("bin key 2 " + binaryKey)

    test= int(test1,2) ^ int(binaryKey,2)
    xor = bin(test)[2:]

    print("xor 2 " + xor)

    result = []
    for index in range(0, len(xor), 7):
        result.append(xor[index : index + 7])

    test = ''
    for i in result:
        test  += chr(int(i, 2))

    print(test)


#encrypt(pw, key)
decrypt(encrypt(pw, key), key)