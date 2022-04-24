from credentials import Credentials
import unittest


class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials(
            "Twitter", "Njau", "njau1234567890#")

    def test_credentials_init(self):
        self.assertEqual(self.new_credentials.platform_name, "Twitter")
        self.assertEqual(self.new_credentials.username, "Njau")
        self.assertEqual(self.new_credentials.password, "njau1234567890#")

    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        Credentials.credentials_list = []

    def test_delete_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter", "jnjauu", "jnjauu1234")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_display_credentials(self):
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

    def test_search_credentials(self):
        self.new_credentials.save_credentials()
        test_search = Credentials("Twitter", "jnjauu", "jnjauu1234")
        test_search.save_credentials()

        found_credentials = Credentials.search_credentials("Twitter")
        self.assertEqual(found_credentials.platform_name, test_search.platform_name)


if __name__ == "__main__":
    unittest.main()
