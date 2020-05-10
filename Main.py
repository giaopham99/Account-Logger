import os
from Commands import *
from Coder import *

# Open file or create file to store info
if os.path.isfile('DO-NOT-DELETE.txt'):
    data = open('DO-NOT-DELETE.txt', mode='r+')
    copy = open('TEMP.txt', mode='r+')
else:
    data = open('DO-NOT-DELETE.txt', mode='x+')
    copy = open('TEMP.txt', mode='x+')


def createshift():
    newshift = input("Enter a number between 1 and 100: ")
    with open("DO-NOT-DELETE.txt", "w") as data:
        data.write(newshift + "\n")
    return newshift


def create_master_pass(shift):  # Create a Master Password
    newpass = input("Enter a master password: ")
    newpass = encrypt(newpass, shift)  # encrypt the master password
    with open("DO-NOT-DELETE.txt", "a") as data:
        data.write(newpass + "\n")


data.close()
copy.close()
# If User is new to the program
if os.path.getsize("DO-NOT-DELETE.txt") == 0:
    shift = createshift()
    create_master_pass(shift)

# Ask for shift and master pass
shift = 0
with open("DO-NOT-DELETE.txt") as data:
    shift = data.readline()
    password = data.readline().strip('\n')
    password = decrypt(password, shift)
userInput = ""
while (userInput != password):
    userInput = input("What is the password? ")
    if userInput != password:
        print("Wrong pass. Try again: ")
    # ADD OPTION TO CHANGE PASS


command = displaymenu()
while command != "q":
    if command == "a":
        retrieve_account(shift)
    elif command == "b":
        addaccount(shift)
    elif command == "c":
        userInput = input("New Password: ")
        updatemaster(userInput, shift)
    elif command == "d":
        updateshift()
    elif command == "e":
        update_account()
    elif command == "f":
        listall()
    else:
        print("Invalid Option")
    command = displaymenu()
