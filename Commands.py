from Coder import *


def displaymenu():
    print("Pick an Option:")
    print("(a) Retrieve an Account Log-in")
    print("(b) Add an Account Log-in")
    print("(c) Update Master Password or shift")
    print("(d) Update an Account")
    print("(e) Quit")
    return input()


def retrieve_account():
    print("retrieved")


def addaccount(file, shift):
    userInput = input("Nickname of Account: ")
    userInput = encrypt(userInput, shift)
    file.write(userInput + " ")
    userInput = input("Username: ")
    userInput = encrypt(userInput, shift)
    file.write(userInput + " ")
    userInput = input("Password: ")
    userInput = encrypt(userInput, shift)
    file.write(userInput + " ")


def updatemaster():
    print("updated master")


def update_account():
    print("updated account")
