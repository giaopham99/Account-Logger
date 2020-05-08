from Coder import *
import os


def displaymenu():
    print("Pick an Option:")
    print("(a) Retrieve an Account Log-in")
    print("(b) Add an Account Log-in")
    print("(c) Update Master Password or shift")
    print("(d) Update an Account")
    print("(e) Quit")
    return input()


def retrieve_account(file, shift):
    account = input("What account are you looking for? ")
    line = search(file, account)
    if line == "0":
        print("Error: Nickname for account does not exist.")
    else:
        line = line.split()
        line = [decrypt(word, shift) for word in line]
        print("Account: " + line[0])
        print("Username: " + line[1])
        print("Password: " + line[2])


def addaccount(file, shift):
    userInput = input("Nickname of Account: ")
    userInput = encrypt(userInput, shift)
    file.write(userInput + " ")
    userInput = input("Username: ")
    userInput = encrypt(userInput, shift)
    file.write(userInput + " ")
    userInput = input("Password: ")
    userInput = encrypt(userInput, shift)
    file.write(userInput + " \n")


def updatemaster():
    print("updated master")


def search(file, account):
    file.seek(os.SEEK_SET, os.SEEK_END)  # find the end
    end = file.tell()
    file.seek(0)  # reset to beginning of file
    shift = file.readline()
    temp = file.readline()
    while file.tell() < end:
        line = file.readline()
        temp = line.split()[0]
        temp = decrypt(temp, shift)
        if temp == account:
            return line
    return "0"


def update_account(file):
    print("What account do you want to update?")
    command = input()
    found = search(file, command)
    if not found == "0":
        print("What do you want to update?")
        print("(a) Nickname")
        print("(b) Username")
        print("(c) Password")
        command = input()
        if command == "a":
            updateNick()
        elif command == "b":
            updateUser()
        elif command == "c":
            updatePass()
        else:
            print("Error: Invalid Option")
    else:
        print("Error: Account not found")


def updateNick():
    return 0


def updateUser():
    return 0


def updatePass():
    return 0
