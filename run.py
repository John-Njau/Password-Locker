#!/usr/bin/python3

from users import User
from credentials import Credentials


def create_user(name,username, password):
    """Function that creates a new user account on the password locker application"""
    new_user = User(name,username, password)
    return new_user

def password_locker():
    print("\n")
    print("Welcome to Password Locker")
    while True:
        print("\n")
        print("Choose an option to continue : \n11 : Create Password Locker account\n22 : Log In to an existing account \n33 : Exit")
        option_code = input("Enter option: ").lower().strip()
        if option_code == "11":
            print("Creating new account \n")
            name= input("Enter your name: ")
            print(name)
            username= input("Enter your preferred username: ")
            print(name + " " + username)
            password = input("Enter your new password: ")
            conf_password = input("confirm your password: ")
            if password == conf_password:
                print(f"Password confirmed successfully\n")
                print(f"New account for {username} created successfully")
                while True:
                    print(f"\n Hello {username}! What to do you want to do today?")
            else:
                print("Passwords do not match")
                print("Please try again")
        elif option_code == "22":
            pass
        elif option_code == "33":
            break


if __name__ == '__main__':
   password_locker()