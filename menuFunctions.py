import functions

# @param: FileWriter
def fnMenu1(*args):
    print("\n\n")
    for i, j in enumerate(args):
        print(i, j[1])
    print("\n\n")

# @param: Encryption Key, Reference to the write Password function
def fnMenu2(*args):
    print("\n\n")
    userInput = input("Enter a new password: (multiple passwords separated with ;)\n")
    arrPasswords = []
    for password in userInput.split(";"):
        arrPasswords.append(functions.fnEncryptString(password, args[0]))
    args[1](arrPasswords)
    print("\n\n")

# @param: FileWriter, Reference to the rewrite File function
def fnMenu3(*args):
    print("\n\n")
    for i, j in enumerate(args[0]):
        print(i, j[1])
    deletePassword = int(input("Which password do you want to delete? (Use number)\n"))
    try:
        args[0].pop(deletePassword)
        args[1]()
        print("\n\n")
    except IndexError:
        print("Please enter a correct password")

# @param: -
def fnMenu4(*args):
        exit()
