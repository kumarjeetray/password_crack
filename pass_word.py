import hashlib
flag = 0
pass_hash = input("Enter md5 hash:")
wordlist = input("File name: ")

try:
    # name of while where the probable passwords are stored.
    pass_file = open(wordlist, "r")
except:
    print("No file found")
    quit()
for word in pass_file:
    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

    if digest == pass_hash:
        print("Password found")
        print("Password:" + word)
        flag = 1
        break

if flag == 0:
    print("Password not in the list")
