#Ablay, John Carlo 
#BSCPE 1-5 2022-09812-MN-0
#Program 2

import emoji 
import pyfiglet as pyg

author_name = ("PROGRAMMED BY: JOHN CARLO ABLAY")
name = author_name.center(100)
print(name)

username  = input("Please enter your name: ")
print("Hello, ", username)

result = pyg.figlet_format("\nCODE DECRYPTOR", font = "digital")
print (result)


moredata = "yes"
while moredata == "yes":
    input_string = input("Enter a word: ")
    print("Encrypted String: ", input_string)

    output_string = input_string.replace('*','a').replace('&','e').replace('#','i').replace('+','o').replace('!','u')     
    print("Decrypted String: ", output_string, "\n")

    moredata = str(input("Would you like to run the program again? (yes or no): \n"))
print("\nThank you for using my program!")
print(emoji.emojize(":grinning_face_with_big_eyes: "))

