from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    
    def setUp(self):
        """Set up the test client and other necessary variables."""
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
    
    def test_home_page(self):
        """Test if the home page loads successfully and displays the board."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Boggle Game', response.data)

    def test_check_word(self):
        """Test the check word functionality."""
        with self.client:
            self.client.get('/')  
            response = self.client.post('/check-word', json={"word": "TEST"})
            self.assertEqual(response.status_code, 200)
            self.assertIn('result', response.json)
