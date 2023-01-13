import hashlib
import progressbar
import time
from functions import fnEncryptString 

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