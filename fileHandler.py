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
    with open(strFileName, mode='a') as objPasswordFile:
        objPasswordFile = csv.writer(objPasswordFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        objPasswordFile.writerow(arrPasswords)
