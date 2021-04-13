import functions

def fnMenu1(passwordArray):
    print("\n\n")
    for i, j in enumerate(passwordArray):
        print(i, j[1])
    print("\n\n")


def fnMenu2(encryptionKey, writePasswordFunctionReference):
    print("\n\n")
    newPassword = input("Enter a new password:\n")
    newPassword = functions.fnEncryptString(
        newPassword, encryptionKey)
    writePasswordFunctionReference(newPassword)
    print("\n\n")


def fnMenu3(passwordArray, rewriteFileFunctionReference):
    print("\n\n")
    for i, j in enumerate(passwordArray):
        print(i, j[1])
    deletePassword = int(input("Which password do you want to delete? (Use number)\n"))
    try:
        passwordArray.pop(deletePassword)
        rewriteFileFunctionReference()
        print("\n\n")
    except IndexError:
        print("Please enter a correct password")

def fnMenu4():
        exit()
