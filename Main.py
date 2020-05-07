import os.path
from Commands import *
from Coder import *

# Open file or create file to store info
data = open('DO-NOT-DELETE.txt', mode='r+')


def createshift():
    newshift = input("Enter a number: ")
    data.write(newshift + "\n")
    return newshift


def create_master_pass(shift):  # Create a Master Password
    newpass = input("Enter a master password: ")
    newpass = encrypt(newpass, shift)  # encrypt the master password
    data.write(newpass + "\n")


# If User is new to the program
if os.path.getsize('DO-NOT-DELETE.txt') == 0:
    shift = createshift()
    create_master_pass(shift)


# Ask for shift and master pass
shift = data.readline()
password = data.readline().rstrip('\n')
password = decrypt(password, shift)
userInput = ""
while (userInput != password):
    userInput = input("What is the password? ")
    userInput = userInput
    if userInput != password:
        print("Wrong pass. Try again: ")

command = displaymenu()
while command != "e":
    if command == "a":
        retrieve_account()
    elif command == "b":
        addaccount(data, shift)
    elif command == "c":
        updatemaster()
    elif command == "d":
        update_account()
    else:
        print("Invalid Option")
    command = displaymenu()
