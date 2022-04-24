class User:
    """
    This is the users class
    """

    def __init__(self, first_name, last_name, username, password):
        """
        Initialize user properties that will be required on 
        setting up a password locker account
        """
        self.first_name = first_name
        self.last_name = last_name
        # self.email = email
        self.username = username
        self.password = password
        self.login_attempts = 0

    user_accounts_list = []

    def save_user_account(self):
        """saves user details to allow them to login later"""
        User.user_accounts_list.append(self)

    def delete_user_account(self):
        User.user_accounts_list.remove(self)

    @classmethod
    def verify_user(cls, username, password):
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
