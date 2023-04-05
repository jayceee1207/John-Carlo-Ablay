#Ablay, John Carlo R.
#BSCPE 1-5 2022-09812-MN-0
#Program 3

author_name = ("PROGRAMMED BY: JOHN CARLO ABLAY")
name = author_name.center(100)
print(name)


import string
import emoji
import pyfiglet
import os
os.system("cls")

dict = {}

#this variable won't be used in the program, this will just be my guide for the letter and its corresponding value.
dict_made = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10,
            'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18, 'T' : 19, 'U' : 20, 'V' : 21,  'W' : 22,
            'X' : 23, 'Y' : 24, 'Z' : 25}

moredata = "yes"
while moredata == "yes":
    
    result = pyfiglet.figlet_format("VIGENERE CIPHER", font = "bubble" )
    print(result)
    #this will enumerate all the ascii value and will be inserted inside the empty dictionary
    for i, char in enumerate(string.ascii_uppercase):
        dict[i] = char

    #make a function named loop_key to get the list of key
    def loop_key(message, key):
        key = list(key)
        if len(message) == len(key):
            return key
        else:
            for i in range(len(message) - len(key)):
                key.append(key[i % len(key)])
        return "".join(key)

    #make a function named cipher_txt to get the list of cipher text

    def cipher_txt(message, key):
        cipher_text = []
        for i in range(len(message)):
            x = (ord(message[i]) + ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        return " ".join(cipher_text)

    def add_bot(message, key):
        add = []
        for i in range(len(message)):
            x = (ord(message[i])-65) + (ord(key[i])-65)
            add.append(x)
        print("Add: ", add)
        return

    def mod_bot(message, key):
        mod = []
        for i in range(len(message)):
            x = ((ord(message[i]) - 65) + (ord(key[i]) - 65)) % 26
            mod.append(x)
        print("Mod: ", mod)
        return


    message = str(input("Message: "))
    keyword = str(input("Key: "))
    key = loop_key(message, keyword)
    cipher_text = cipher_txt(message, key)

    num_message = ""
    num_key = ""

    for char in message:
        for num, letter in dict.items():
            if char == letter:
                num_message += str(num)
                num_message += " "

    for char in key:
        for num, letter in dict.items():
            if char == letter:
                num_key += str(num)
                num_key += " "

    print("\u001b[33;1m","Message: ", message, num_message)
    print("\u001b[33;1m","Key: ", keyword, num_key)

    sum = add_bot(message, key)
    mod = mod_bot(message, key)

    print("\u001b[32;1m","Add: ", sum) 
    print("\u001b[32;1m","Mod: ", mod)

    print("\u001b[37;1m","Ciphertext", cipher_text)

    moredata = str(input("Do you want to try again? (yes or no): "))

print("\nThank you for using my program!")
print(emoji.emojize(":grinning_face_with_big_eyes:"))
