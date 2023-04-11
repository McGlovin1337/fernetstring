import unittest
from cryptography import fernet
from fernetstring import fernetstr, keyfuncs


class TestFernetString(unittest.TestCase):
    """Test the FernetString Class"""

    def test_is_bytes(self):
        """Test that the secure_string property is of type bytes"""
        test_str = 'TestString'
        fstr = fernetstr.FernetString(test_str)
        self.assertTrue(isinstance(fstr.secure_string, bytes))

    def test_decryption(self):
        """Test that the decrypted string matches the original string"""
        test_str = 'TestString'
        fstr = fernetstr.FernetString(test_str)
        self.assertEqual(fstr.decrypt(), test_str)

    def test_no_input(self):
        """Test that exception is thrown when no input string is provided"""
        self.assertRaises(TypeError, fernetstr.FernetString)

    def test_decryption_differing_key(self):
        """Test that exception is thrown when attempting to decrypt with a different key"""
        test_str = 'TestString'
        fstr = fernetstr.FernetString(test_str)
        self.assertRaises(fernet.InvalidToken, fstr.decrypt, keyfuncs.test_key())

    def test_create_object_from_secure_string(self):
        """Create a new FernetString object from an existing secure_string"""
        test_str = 'TestString'
        fstr = fernetstr.FernetString(test_str)
        new_fstr = fernetstr.FernetString(fstr.secure_string)

        self.assertTrue(isinstance(new_fstr, fernetstr.FernetString))
        self.assertEqual(new_fstr.decrypt(), test_str)


if __name__ == '__main__':
    unittest.main()
