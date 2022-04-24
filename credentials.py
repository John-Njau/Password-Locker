from random import *


class Credentials:
    """User credentials class, save information and generate passwords"""

    def __init__(self, platform_name, username, password):
        """Initializing the credentials class"""
        self.platform_name = platform_name
        self.username = username
        self.password = password
        #

    credentials_list = []

    def save_credentials(self):
        """Method to save credentials"""
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """Method that allows a user to delete existing credentials"""
        Credentials.credentials_list.remove(self)

    def gen_password(ln):
        """Generating a random password"""
        chars = "ABCDEFGHIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*</>|"
        password = ""
        for i in range(ln):
            password += chars[randint(0, len(chars) - 1)]
        return password

    @classmethod
    def display_credentials(cls):
        """Returns all saved credentials"""
        return cls.credentials_list

    @classmethod
    def search_credentials(cls, platform_name):
        """Method that takes in the platform name and searches for existing credentials in the credentials list"""
        for credential in cls.credentials_list:
            if credential.platform_name == platform_name:
                return credential
