# name: Shelly
#date: Dec 18
# purpose:  to make the password Generator for two steps
# This code will create a program that will generate secure passwords. We use generate a random password and generate a passphrase from randam words two steps



import random

lower_letters = ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']                                             #List of the different character types for creating passwords

print("press 1 to generate a random password")
print("press 2 to generate a passphrase from random words")
user_choose = int(input("What is your choice(1 or 2)"))                                             #ask user which one do you what to choose to make the passwords

if user_choose == 1:                                                                                # to  make which game do the user what to play
    password_length = int(input("What is the numbers of characters your password should be?"))      # Get the length of the sentence

    lower_letters_choice = input("Would you like to have lower case letters(y/n)?")                 #Write lower letters  to get what the user wants
    upper_letters_choice = input("Would you like to have upper case letters(y/n)?")                 #ask the user  do  the password need upperer letters

    numbers_choice = input("Would you like to have numbers(y/n)?")                                  #ask the user  do  the password need numbers
    symbols_choice= input("Would you like to have symbols(y/n)?")                                   #ask the user  do  the password need symbols

    all_keys = []                                                                                   #Create a blank list to generate the password into.
    if lower_letters_choice == "y":                                                                 #to check choice whether is "y",
        all_keys = all_keys + lower_letters                                                         #it is like x=x+1 code, make sure the code is right
    if upper_letters_choice == "y":
        all_keys = all_keys + upper_letters
    if numbers_choice == "y":
        all_keys = all_keys + numbers
    if symbols_choice == "y":
        all_keys = all_keys + symbols

    password = ""                                                                                   # to do the string function, and make the code set up
    for i in range(0, password_length):                                                             # use for make a loop
        password = password + random.choice(all_keys)
    print(password)

    au = input("Would you like to substitute numbers or symbols for letters?(y/n)?")                # also a user yje subsyritute numbers
    if au == "y":
        password = password.replace("o", "0")                                          #to replace letter to numbers and symbol
        password = password.replace("i", "!")
        password = password.replace("e","3")
        password = password.replace("a","@")
        password = password.replace("c","(")
        password = password.replace("s","5")                                           #make six letters
        print(password)
    else:
        print("You are wrong")


elif user_choose == 2:                                                                               # start the second game
    ask = int(input("How many words should your passphrase contain?"))                               # to ask the user
    file = open("engmix.txt","r",encoding='utf-8', errors='ignore')                                  #to make a new file, and use open function.And it can to use the new file words
    word_list = file.readlines()
    file.close()                                                                                     #to make a new file close
    password = ""
    for i in range(ask):                                                                             #to make a loop for the passwords
        password = password + random.choice(word_list).strip()
    print("You password is", password)
    au = input("Would you like to substitute numbers or symbols for letters?(y/n)?")                 # it is same for first game, to replace the letter to numbers and sysmbols
    if au == "y":
        password = password.replace("o", "0")
        password = password.replace("i", "!")
        password = password.replace("e","3")
        password = password.replace("a","@")
        password = password.replace("c","(")
        password = password.replace("s","5")
        print("Your new password is",password)





