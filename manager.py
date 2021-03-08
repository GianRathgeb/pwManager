

pw = "Password"
key = "encrypt"

binaryPW = [bin(ord(char)) for char in pw]
test = ''
for char in binaryPW:
    test += char.replace('0b', '')

binaryPW =  test

binaryKey = [bin(ord(char)) for char in key]
test = ''
for char in binaryKey:
    test += char.replace('0b', '')

# repeat key until 
binaryKey = (test * (int(len(binaryPW)/len(test))+1))[:len(binaryPW)]



test= int(binaryPW,2) ^ int(binaryKey,2)
xor = bin(test)[2:]

print(xor)