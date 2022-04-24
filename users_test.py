import unittest
from users import User


class TestUser(unittest.TestCase):
    """
    Test class for the user class
    """

    def setUp(self):
        """
        Runs before each user class is created to
        initialize the variables to be found inside the user class, it sort
        of sets us the benchmark for the user class
        """

        # creating a user object
        self.new_user = User(
            "John", "JohnMichaels",
            "MichaelQuienv1234#"
        )

    def test_init(self):
        """Testing if the user object is initialized properly"""
        self.assertEqual(self.new_user.name, "John")
        # self.assertEqual(self.new_user.last_name, "Njau")
        # self.assertEqual(self.new_user.email, "jd@mura.com")
        self.assertEqual(self.new_user.username, "JohnMichaels")
        self.assertEqual(self.new_user.password, "MichaelQuienv1234#")

    def test_save_user_account(self):
        """Save user User to the system so that they can be used"""
        self.new_user.save_user_account()
        self.assertEqual(len(User.user_accounts_list), 1)

    def tearDown(self):
        """
        Cleaning up after running a test, without the tearDown method,
        the test will fail as there is a trailing saved user that adds 
        a +1 to the saved users
        """
        User.user_accounts_list = []

    def test_delete_user_account(self):
        """Deleting one's password locker account"""
        self.new_user.save_user_account()
        test_user_account = User(
            "John", "JohnMichaels", "MagixEngry1234#")
        test_user_account.save_user_account()
        self.new_user.delete_user_account()
        self.assertEqual(len(User.user_accounts_list), 1)

    def test_verify_user(self):
        # self.new_User.save_User()
        self.new_user = User("John", "jnjauu", "jnjauu1234")
        self.new_user.save_user_account()
        another_user = User("John", "jnjauu", "jnjauu1234")
        another_user.save_user_account()

        for user in User.user_accounts_list:
            if user.username == another_user.username and user.password == another_user.password:
                current_user = user.username
                return current_user

        # self.assertEqual(current_user, User.verify_user(
        #     another_user.username, another_user.password))


if __name__ == "__main__":
    unittest.main()
