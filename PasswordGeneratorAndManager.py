import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?0123456789'

def create():
    newPwd = ''
    global savedPwd
    print('How many characters would you like in this password?\n')
    lengthPwd = input()
    lengthPwd = int(lengthPwd)
    for i in range(lengthPwd):
        newPwd += random.choice(chars)
    print("Here is your generated password: ", newPwd)
    savedPwd = newPwd
    
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            username, password = data.split("|")
            print("Account Name:", username, "\n", "Password:", password)
        
def add():
    password = ''
    username = input("Account Name: ")
    importPwd = input("Would you like to use last generated password? [Enter y or n]")
    if (importPwd == 'y'):
        if (savedPwd == ''):
            print("There was no password generated.")
            return
        else:
            password = savedPwd
            print('Account and Password successfully saved.')
    elif (importPwd == 'n'):
        password = input("Password: ")
    
    with open("passwords.txt", 'a') as f:
        f.write(username + "|" + password + "\n")

while True:
    mode = input("Are we creating a password, adding a password or viewing current passwords? ['create', 'add', 'view', 'q'] ")
    if mode == "q":
        break  
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    elif mode == "create":
        create()