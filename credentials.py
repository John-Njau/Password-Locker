class Credentials:
    """User credentials class, save information and generate passwords"""
    def __init__(self,account_name, username, password):
        """Initializing the credentials class"""
        self.account_name = account_name
        self.username = username
        self.password = password
        #
    credentials_list = []
    def save_credentials(self):
        Credentials.credentials_list.append(self)