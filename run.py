from random import randint

def mainMenu():
    print("1. Encrypt file\n2. Decrypt file\n3. Extended encrypt\n4. exit")
    userchoice = input("Select an option: ")
    if userchoice == "1":
        plaintext = readFile()
        print("Encrypted text:", encrypt(plaintext))
    elif userchoice == "2":
        ciphertext = readFile()
        print("Decrypted text:", decrypt(ciphertext))
    elif userchoice == "3":
        plaintext = readFile()
        print("Encrypted text:", extendedEncrypt(plaintext))
    elif userchoice == "4":
        exit()
    else:
        exit()

def readFile():
    filename = input("filename?: ")
    contents = open(filename, 'r')
    return(contents.read())

def writeFile(contents):
    filename = input("Save to file?")
    fileopen = open(filename, "w")
    fileopen.write(contents)
    fileopen.close()

def genKey():
    count = 0
    key = ""
    while count < 8:
        keychar = chr(randint(33,126))
        count += 1
        key += keychar
    print("Key:", key)
    return(key)

def calcOffset(key):
    ascii = 0
    for char in key:
        ascii += ord(char)
    return(int(ascii/8)-32)

def encrypt(plaintext):
    key = genKey()
    offset = calcOffset(key)
    ciphertext = ""
    for char in plaintext:
        if char == " ":
            ciphertext += " "
        else:
            assoff = ord(char) + offset 
            if assoff > 126:
                assoff -= 94
            ciphertext += chr(assoff)
    writeFile(ciphertext)
    return ciphertext

def decrypt(ciphertext):
    key = input("Key: ")
    offset = calcOffset(key)
    plaintext = ""
    for char in ciphertext:
        if char == " ":
            plaintext += " "
        else:
            assoff = ord(char) - offset
            if assoff  < 33:
                assoff += 94
            plaintext += chr(assoff)
    return plaintext

def extendedEncrypt(plaintext):
    key = genKey()
    offset = calcOffset(key)
    ciphertext = ""
    count = 0
    plaintext.replace(" ", "")
    for char in plaintext:
        count += 1
        assoff = ord(char) + offset
        if count %5 == 0:
            ciphertext += " "
        elif assoff > 126:
            assoff -= 94
        ciphertext += chr(assoff)
    writeFile(ciphertext)
    return ciphertext

mainMenu()
