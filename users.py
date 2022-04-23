class User:
    """
    This is the users class
    """

    def __init__(self, first_name, last_name, email, username, password):
        """
        Initialize user properties that will be required
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.login_attempts = 0

    accounts = []
    def save_user(self):
        """saves user details to allow them to login later"""
        User.accounts.append(self)
#     def genPassword():
#     def existing_account(): 
#     def login(self, username, password):
#         """ checks whether the username and password are correct """


# new_user = User("John", "Njau", "jd@mura.com")
# print(new_user.__dict__)
# print(new_user.__sizeof__())
# print(new_user.__doc__)
# print(new_user.__module__)
# print(new_user.__init_subclass__)
