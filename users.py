class User:
    """
    This is the users class
    """

    def __init__(self, first_name, last_name, email, username, password):
        """
        Initialize user properties that will be required on 
        setting up a password locker account
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.login_attempts = 0

    accounts_list = []

    def save_user_account(self):
        """saves user details to allow them to login later"""
        User.accounts_list.append(self)

    def delete_user_account(self):
        User.accounts_list.remove(self)

# new_user = User("John", "Njau", "jd@mura.com")
# print(new_user.__dict__)
# print(new_user.__sizeof__())
# print(new_user.__doc__)
# print(new_user.__module__)
# print(new_user.__init_subclass__)
