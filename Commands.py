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
    return input().strip()


def retrieve_account(shift):
    with open("DO-NOT-DELETE.txt") as data:
        end = findEnd(data)
        data.readline()
        data.readline()
        if data.tell() == end:
            return print("Error: You have no accounts logged.")
        account = input("What account are you looking for? ").strip()
        line = search(data, account)
        if line == "0":
            print("Error: Account name does not exist.")
        else:
            line = line.split()
            line = [decrypt(word, shift) for word in line]
            print("Account: " + line[0])
            print("Username: " + line[1])
            print("Password: " + line[2])


def addaccount(shift):
    account = input("Account Name: ").strip()
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
            command = input(
                "(a) Add a different account\n(b) Update this Account").strip()
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
    if int(currentshift) < int(newshift):
        shift = int(newshift)-int(currentshift)
        if len(line) == 1:  # master password
            return encrypt(code, shift) + "\n"
        nickname = encrypt(line[0], shift)
        username = encrypt(line[1], shift)
        password = encrypt(line[2], shift)
        return nickname + " " + username + " " + password + "\n"
    elif int(currentshift) > int(newshift):
        shift = int(currentshift)-int(newshift)
        if len(line) == 1:  # master password
            return decrypt(code, shift) + "\n"
        nickname = decrypt(line[0], shift)
        username = decrypt(line[1], shift)
        password = decrypt(line[2], shift)
        return nickname + " " + username + " " + password + "\n"
    else:
        return code


def updateshift(newshift):
    with open("DO-NOT-DELETE.txt", "r") as data:
        with open("TEMP.txt", "w+") as copy:
            end = findEnd(data)
            while data.tell() < end:
                copy.write(data.readline())
    with open("DO-NOT-DELETE.txt", "w+") as data:
        with open("TEMP.txt", "r") as copy:
            end = findEnd(copy)
            data.write(str(newshift) + "\n")  # new shift
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
            print("(a) Account Name")
            print("(b) Username")
            print("(c) Password")
            command = input().strip()
            if command == "a":
                userInput = input("New Account Name: ")
                updater(userInput, account, 0)
            elif command == "b":
                userInput = input("New Username: ")
                updater(userInput, account, 1)
            elif command == "c":
                userInput = input("New Password: ")
                updater(userInput, account, 2)
            else:
                print("Error: Invalid Option")
        else:
            print("Error: Account not found")


def updater(new, account, pos):
    with open("DO-NOT-DELETE.txt", "r+") as data:
        with open("TEMP.txt", "w+") as copy:
            end = findEnd(data)
            while data.tell() < end:
                copy.write(data.readline())
    with open("DO-NOT-DELETE.txt", "w+") as data:
        with open("TEMP.txt", "r+") as copy:
            end = findEnd(copy)
            shift = copy.readline()
            data.write(shift)  # copy shift over
            data.write(copy.readline())  # copy master password over
            while copy.tell() < end:
                original = copy.readline()  # used to copy over if no changes needed
                line = original.split()  # used to find the name of account
                # if this is the right account name for the account that will be updated
                if line[0] == encrypt(account, shift):
                    # change the correct category
                    line[pos] = encrypt(new, shift)
                    data.write(line[0] + " " + line[1] + " " + line[2] + "\n")
                else:
                    data.write(original)


def listall():
    with open("DO-NOT-DELETE.txt", "r") as data:
        end = findEnd(data)
        data.readline()  # skipping the shift
        data.readline()  # skipping the master password
        if data.tell() == end:
            print("No accounts available.")
        while data.tell() < end:
            line = data.readline().split()
            print("Account: " + line[0])
            print("Username: " + line[1])
            print("Passsword: " + line[2] + "\n")
