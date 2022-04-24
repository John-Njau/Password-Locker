class User:
    """
    This is the users class
    """

    user_accounts_list = []

    def __init__(self, name, username, password):
        """
        Initialize user properties that will be required on 
        setting up a password locker account
        """
        self.name = name
        self.username = username
        self.password = password

    def save_user_account(self):
        """saves user details to allow them to login later"""
        User.user_accounts_list.append(self)

    def delete_user_account(self):
        User.user_accounts_list.remove(self)

    @classmethod
    def check_user(cls, username, password):
        current_user = " "
        for user in User.user_accounts_list:
            if user.username == username and user.password == password:
                current_user = user.username
        return current_user

# new_user = User("John", "Njau", "jd@mura.com")
# print(new_user.__dict__)
# print(new_user.__sizeof__())
# print(new_user.__doc__)
# print(new_user.__module__)
# print(new_user.__init_subclass__)
