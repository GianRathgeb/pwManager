import csv
class FileWriter:
    def __init__(self, fileName):
        self.strFileName = fileName

    def fnReadPasswords(self):
        with open(self.strFileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            self.arrPasswords = []
            for row in csv_reader:
                try:
                    self.arrPasswords.append(row[0])
                except IndexError:
                    print("No Passwords found in file")
        
    def fnWritePassword(self, strPassword):
        with open(self.strFileName, mode='a+') as objPasswordFile:
            objPasswordFile.write(f"\n{strPassword}")

    def fnRewriteFile(self, strPasswordHash, arrPasswords):
        with open(self.strFileName, mode='w') as objPasswordFile:
            strToWrite = f"{strPasswordHash}"
            for i in arrPasswords:
                strToWrite += f"\n{i[0]}"
            objPasswordFile.write(strToWrite)

