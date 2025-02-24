import unittest
from app import app

class TestFlaskAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_prime_true(self):
        response = self.app.get('/is_prime/11')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'true')

    def test_prime_false(self):
        response = self.app.get('/is_prime/12')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'false')

if __name__ == '__main__':
    unittest.main()    
    # def test_plus(self):
    #     response = self.app.get('/plus/5/6')
    #     self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data.decode('utf-8'), '11')

# if __name__ == '__main__':
#     unittest.main()
