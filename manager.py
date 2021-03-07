

pw = "Password"
key = "Encrypt"

binaryPW = [bin(ord(char)) for char in pw]
test = ''
for char in binaryPW:
    test += char.replace('0b', '')

binaryPW =  bin(int(test, 2))

binaryKey = [bin(ord(char)) for char in pw]
test = ''
for char in binaryPW:
    test += char.replace('0b', '')

binaryKey = bin(int(test, 2))

print(type(binaryPW))
print(binaryKey)

print(binaryPW ^ binaryKey)
