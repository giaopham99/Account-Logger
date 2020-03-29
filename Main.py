import os.path


def displaymenu():
    print("Pick an Option:")
    print("(a) Retrieve an Account Log-in")
    print("(b) Add an Account Log-in")
    print("(c) Update Master Password")
    print("(d) Update an Account")
    return input()


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
