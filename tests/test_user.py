import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('testuser', 'password')
        self.user.deposit(100)

    def test_get_username(self):
        self.assertEqual(self.user.get_username(), 'testuser')

    def test_set_password(self):
        self.user.set_password('newpassword')
        self.assertTrue(self.user.verify_password('newpassword'))

    def test_deposit(self):
        self.user.deposit(50)
        self.assertEqual(self.user.get_balance(), 150)

    def test_withdraw_success(self):
        self.user.withdraw(50)
        self.assertEqual(self.user.get_balance(), 50)

    def test_withdraw_failure(self):
        self.user.withdraw(150)
        self.assertEqual(self.user.get_balance(), 100)

    def test_verify_password(self):
        self.assertTrue(self.user.verify_password('password'))
        self.assertFalse(self.user.verify_password('wrongpassword'))

if __name__ == '__main__':
    unittest.main()

