import os
from Commands import *
from Coder import *

# Open file or create file to store info
if os.path.isfile('DO-NOT-DELETE.txt'):
    data = open('DO-NOT-DELETE.txt', mode='r+')
else:
    data = open('DO-NOT-DELETE.txt', mode='x+')


def createshift():
    newshift = input("Enter a number between 1 and 100: ")
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
data.seek(0)
shift = data.readline()
password = data.readline().rstrip('\n')
password = decrypt(password, shift)
userInput = ""
while (userInput != password):
    userInput = input("What is the password? ")
    userInput = userInput
    if userInput != password:
        print("Wrong pass. Try again: ")
    # ADD OPTION TO CHANGE PASS


command = displaymenu()
while command != "e":
    if command == "a":
        retrieve_account(data, shift)
    elif command == "b":
        addaccount(data, shift)
    elif command == "c":
        updatemaster()
    elif command == "d":
        update_account(data)
    else:
        print("Invalid Option")
    command = displaymenu()
