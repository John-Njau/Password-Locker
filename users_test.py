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
            "John", "Njau", "jd@mura.com", "JohnMichaels",
            "MichaelQuienv1234#"
        )

    def test_init(self):
        """Testing if the user object is initialized properly"""
        self.assertEqual(self.new_user.first_name, "John")
        self.assertEqual(self.new_user.last_name, "Njau")
        self.assertEqual(self.new_user.email, "jd@mura.com")
        self.assertEqual(self.new_user.username, "JohnMichaels")
        # self.assertEqual(self.new_user.password, "MichaelQuienv1234#")
    
    def test_save_user_(self):
        """Save user credentials to the system so that they can be used"""
        self.new_user.save_user()
        self.assertEqual(len(User.accounts), 1)


if __name__ == "__main__":
    unittest.main()
