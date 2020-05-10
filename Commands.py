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
    account = input("Nickname of Account: ").strip()
    found = ""
    with open("DO-NOT-DELETE.txt", "r+") as data:
        # check to see if account already exists
        found = search(data, account)
        if found == "0":
            data.write(account + " ")
            userInput = input("Username: ")
            userInput = encrypt(userInput.strip(), shift)
            data.write(userInput + " ")
            userInput = input("Password: ")
            userInput = encrypt(userInput.strip(), shift)
            data.write(userInput + " \n")

    if not found == "0":
        print("Error: This account already exists.")
        command = ""
        while not command == "a" and not command == "b":
            print("(a) Add a different account\n(b) Update this Account")
            command = input()
            if command == "a":
                addaccount(shift)
            elif command == "b":
                update_account(account)
            else:
                print("Invalid Option")


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
                data.write(copy.readline())  # copy everything else


def updateEncryption(code, currentshift, newshift):
    line = code.split()
    if currentshift < newshift:
        if len(line) == 1:
            return encrypt(code, int(newshift)-int(currentshift)) + "\n"
        nickname = encrypt(line[0], int(newshift)-int(currentshift))
        username = encrypt(line[1], int(newshift)-int(currentshift))
        password = encrypt(line[2], int(newshift)-int(currentshift))
        return nickname + " " + username + " " + password + "\n"
    elif currentshift > newshift:
        if len(line) == 1:
            return decrypt(code, int(currentshift)-int(newshift)) + "\n"
        nickname = decrypt(line[0], int(currentshift)-int(newshift))
        username = decrypt(line[1], int(currentshift)-int(newshift))
        password = decrypt(line[2], int(currentshift)-int(newshift))
        return nickname + " " + username + " " + password + "\n"


def updateshift(newshift):
    with open("DO-NOT-DELETE.txt", "r+") as data:
        with open("TEMP.txt", "w+") as copy:
            end = findEnd(data)
            while data.tell() < end:
                copy.write(data.readline())
    with open("DO-NOT-DELETE.txt", "w+") as data:
        with open("TEMP.txt", "r+") as copy:
            end = findEnd(copy)
            data.write(newshift + "\n")  # new shift
            oldshift = copy.readline()
            while copy.tell() < end:
                # copy everything else
                data.write(updateEncryption(
                    copy.readline().strip("\n"), oldshift, newshift))


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


def update_account(account):
    with open("DO-NOT-DELETE.txt", "r+") as data:
        if not search(data, account) == "0":
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
