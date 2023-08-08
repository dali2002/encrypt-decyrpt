import tkinter
from tkinter import filedialog

name_pattern = [
    "  _  _  _  _  _ ",
    " / \\/ \\/ \\/ \\/ \\",
    "( BlackSecurity )",
    " \\_/\\_/\\_/\\_/\\_/"
]

for row in name_pattern:
    print(row)

def encrypt(word):
    #word = input("enter here : ")
    crypt_word = ""
    swip = ""
    for i in range(len(word)):
        number = ord(word[i])
        number  = number +1
        swip +=chr(number)
        i +=1
    crypt_word +=swip
    return crypt_word
def decrypt(word):
    decrypt = ""
    swip = ""
    for i in range(len(word)):
        number = ord(word[i])
        number = number-1
        swip += chr(number)
        i +=1
    decrypt += swip
    return decrypt
#folderSelected = filedialog.askdirectory()
f = open("encryptfile.txt","w")
f1 = open("decryptfile.txt","w")
first = input("enter what u wanna encrypt : ")
encryptFirst = encrypt(first)
f.write(str(encryptFirst+'\n'))
answer = input("do u wanna decrypt the file to see what it have inside again ? o/n")
if answer == "o":
    decryptSecond = decrypt(encryptFirst)
    f1.write(str(decryptSecond))
f.close()
f1.close()
print("done ")

