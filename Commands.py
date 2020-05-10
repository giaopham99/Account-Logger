from Coder import *
import os


def displaymenu():
    print("\nPick an Option:")
    print("(a) Retrieve an Account Log-in")
    print("(b) Add an Account Log-in")
    print("(c) Update Master Password")
    print("(d) Update shift")
    print("(e) Update an Account")
    print("(f) List all Accounts")
    print("(q) Quit")
    return input()


def retrieve_account(shift):
    with open("DO-NOT-DELETE.txt") as data:
        end = findEnd(data)
        data.readline()
        data.readline()
        if data.tell() == end:
            return print("Error: You have no accounts logged.")
        account = input("What account are you looking for? ")
        line = search(data, account)
        if line == "0":
            print("Error: Nickname for account does not exist.")
        else:
            line = line.split()
            line = [decrypt(word, shift) for word in line]
            print("Account: " + line[0])
            print("Username: " + line[1])
            print("Password: " + line[2])


def addaccount(shift):
    with open("DO-NOT-DELETE.txt", "a") as data:
        userInput = input("Nickname of Account: ")
        userInput = encrypt(userInput.strip(), shift)
        data.write(userInput + " ")
        userInput = input("Username: ")
        userInput = encrypt(userInput.strip(), shift)
        data.write(userInput + " ")
        userInput = input("Password: ")
        userInput = encrypt(userInput.strip(), shift)
        data.write(userInput + " \n")


def findEnd(file):
    file.seek(os.SEEK_SET, os.SEEK_END)  # find the end
    end = file.tell()
    file.seek(0)  # reset to beginning of file
    return end


def updatemaster(newpass, shift):
    with open("DO-NOT-DELETE.txt", "r+") as data:
        with open("TEMP.txt", "w+") as copy:
            end = findEnd(data)
            while data.tell() < end:
                copy.write(data.readline())
    with open("DO-NOT-DELETE.txt", "w+") as data:
        with open("TEMP.txt", "r+") as copy:
            end = findEnd(copy)
            data.write(copy.readline())  # copy shift over
            copy.readline()
            data.write(decrypt(newpass, shift) + "\n")  # new pass
            while copy.tell() < end:
                data.write(copy.readline())


def updateshift():
    return 0


def search(file, account):
    end = findEnd(file)
    shift = file.readline()
    file.readline()
    while file.tell() < end:
        line = file.readline()
        temp = line.split()[0]
        temp = decrypt(temp, shift)
        if temp == account:
            return line
    return "0"


def update_account():
    with open("DO-NOT-DELETE.txt", "r+") as data:
        print("What account do you want to update?")
        command = input()
        found = search(data, command)
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


def listall():
    return 0
