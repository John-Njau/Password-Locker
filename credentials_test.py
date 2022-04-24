from credentials import Credentials
import unittest


class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials("Twitter", "Njau", "njauGoat1234567890#")

    def test_credentials_init(self):
        self.assertEqual(self.new_credentials.account_name, "Twitter")
        self.assertEqual(self.new_credentials.username, "Njau")
        self.assertEqual(self.new_credentials.password, "njauGoat1234567890#")
        
    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)
        


if __name__ == "__main__":
    unittest.main()
