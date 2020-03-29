import os.path
from Commands import *

# Open file or create file to store info
if os.path.isfile('DO-NOT-DELETE.txt'):
    data = open('DO-NOT-DELETE.txt', mode='r+')
else:
    data = open('DO-NOT-DELETE.txt', mode='x')

# Create a Master Password for empty files
if os.path.getsize('DO-NOT-DELETE.txt') == 0:
    newpass = input("Enter a master password: ")
    data.write(newpass)

# Ask for master pass
password = None
readpass = data.readline()
while (readpass != password):
    password = input("What is the password? ")
    if readpass == password:
        command = displaymenu()
    else:
        print("Wrong pass. Try again: ")

while command != "e":
    if command == "a":
        retrieve_account()
    elif command == "b":
        addaccount()
    elif command == "c":
        updatemaster()
    elif command == "d":
        update_account()
    else:
        print("Invalid Option")
