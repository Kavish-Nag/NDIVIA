import numpy as np
import pandas as pd
data = pd.read_csv("login.csv")
info = data.to_dict(orient='records')
def username_exists(username):
    for user in info:
        if 'user' in user and user['user'] == username:
            return True
    return False

def home():
    print("Hello,", n)
    print("------MENU------")
    print(" 1. Register","\n","2. Login","\n","3. Exit")
    ch = int(input("Enter choice:"))
    if ch==1:
        register()
    elif ch==2:
        login()
    else:
        exit()

def register():
    print("Please register yourself.")
    user=input("Create a username:")
    if username_exists(user):
        print("Username already taken.")
        register()
    else:
        password=input("Create your password:")
        new={"user":user,"password":password}
        info.append(new)
        # Updating the DataFrame
        df = pd.DataFrame(info)
        df.to_csv('login.csv', index=False)
        print("Registered successfully")
        home()

def login():
    print("LOGIN")
    user=input("Enter your username:")
    for existing in info:
        if 'user' in existing and existing['user'] == user:
            password=input("Enter your password:")
            if password == existing['password']:
                print("Login successful.")
                home()
            else:
                print("Incorrect password.")
                login()
            return
    print("You haven't registered.")
    register()

n=(input("Please enter your name:"))
while True:
    home()

