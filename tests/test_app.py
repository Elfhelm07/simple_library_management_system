import unittest
import json
import logging
from app import app

logging.basicConfig(level=logging.INFO)

class TestLibraryAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.token = "Bearer mysecrettoken"

    def test_add_book(self):
        logging.info("Testing adding a book...")
        response = self.app.post('/books', 
                                 headers={'Authorization': self.token}, 
                                 json={'title': '1984', 'author': 'George Orwell'})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Book added successfully!', response.data)

    def test_get_books(self):
        logging.info("Testing getting books...")
        self.app.post('/books', 
                      headers={'Authorization': self.token}, 
                      json={'title': '1984', 'author': 'George Orwell'})
        response = self.app.get('/books?page=1&per_page=10', 
                                headers={'Authorization': self.token})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1984', response.data)

    def test_add_member(self):
        logging.info("Testing adding a member...")
        response = self.app.post('/members', 
                                 headers={'Authorization': self.token}, 
                                 json={'name': 'John Doe'})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Member added successfully!', response.data)

    def test_get_members(self):
        logging.info("Testing getting members...")
        self.app.post('/members', 
                      headers={'Authorization': self.token}, 
                      json={'name': 'John Doe'})
        response = self.app.get('/members', 
                                headers={'Authorization': self.token})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Doe', response.data)

if __name__ == '__main__':
    unittest.main()