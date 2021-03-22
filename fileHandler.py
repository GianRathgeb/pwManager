import csv

def fnReadPasswords(strFileName):
    with open(strFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        arrPasswords = []
        for row in csv_reader:
            try:
                arrPasswords.append(row[0])
            except IndexError:
                print("No Passwords found in file")
        return arrPasswords
    
def fnWritePassword(strFileName, strPassword):
    with open(strFileName, mode='a+') as objPasswordFile:
        objPasswordFile.write(f"\n{strPassword}")

def fnRewriteFile(strFileName, strPasswordHash, arrPasswords):
    with open(strFileName, mode='w') as objPasswordFile:
        strToWrite = f"{strPasswordHash}"
        for i in arrPasswords:
            strToWrite += f"\n{i[0]}"
        objPasswordFile.write(strToWrite)

