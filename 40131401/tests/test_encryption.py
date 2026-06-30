import unittest
from src.encryption import EncryptionManager

class TestEncryption(unittest.TestCase):
    def test_encryption_exists(self):
        manager = EncryptionManager()
        self.assertIsNotNone(manager)

if __name__ == '__main__':
    unittest.main()