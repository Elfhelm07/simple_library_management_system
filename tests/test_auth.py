import unittest
import logging
from app import app

logging.basicConfig(level=logging.INFO)

class TestAuthAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.token = "Bearer mysecrettoken"

    def test_access_with_valid_token(self):
        logging.info("Testing access with a valid token...")
        response = self.app.get('/books?page=1&per_page=10', 
                                headers={'Authorization': self.token})
        self.assertEqual(response.status_code, 200)

    def test_access_with_invalid_token(self):
        logging.info("Testing access with an invalid token...")
        response = self.app.get('/books?page=1&per_page=10', 
                                headers={'Authorization': 'Bearer invalidtoken'})
        self.assertEqual(response.status_code, 403)
        self.assertIn(b'Token is missing or invalid!', response.data)

    def test_access_without_token(self):
        logging.info("Testing access without a token...")
        response = self.app.get('/books?page=1&per_page=10')
        self.assertEqual(response.status_code, 403)
        self.assertIn(b'Token is missing or invalid!', response.data)

if __name__ == '__main__':
    unittest.main()