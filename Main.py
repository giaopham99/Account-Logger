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
    newshift = -1
    while newshift < 0:
        newshift = int(input("Enter a number between 1 and 100: "))
        if newshift < 0:
            print("Invalid shift.")
    with open("DO-NOT-DELETE.txt", "w") as data:
        data.write(str(newshift) + "\n")
    return newshift


def create_master_pass(shift):  # Create a Master Password
    newpass = input("Enter a master password: ").strip()
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
        print("Account has been added.")
    elif command == "c":
        userInput = input("New Password: ").strip()
        updatemaster(userInput, shift)
        print("Master password has been updated.")
    elif command == "d":
        newshift = -1
        while int(newshift) < 0:
            newshift = input("New Shift: ")
            if int(newshift) < 0:
                print("Invalid shift.")
        updateshift(newshift)
        print("Shift has been updated.")
    elif command == "e":
        userInput = input("What account do you want to update? ").strip()
        update_account(userInput)
    elif command == "f":
        listall()
    else:
        print("Invalid Option")
    command = displaymenu()
