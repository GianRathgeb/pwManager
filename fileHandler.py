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
    
def fnWritePassword(strFileName, arrPasswords):
    with open(strFileName, mode='a+') as objPasswordFile:
        for i in arrPasswords:
            objPasswordFile.write(f"\n{i}")
