import unittest
from app import app

class TestFlaskAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_x_is_1(self):
        response = self.app.get('/cir_sur/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '12.56')

    def test_x_is_neg10(self):
        response = self.app.get('/cir_sur/-10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '0.00')


    def test_x_is_1dot5(self):
        response = self.app.get('/cir_sur/1.5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '28.26')

if __name__ == '__main__':
    unittest.main()    
    # def test_plus(self):
    #     response = self.app.get('/plus/5/6')
    #     self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data.decode('utf-8'), '11')

# if __name__ == '__main__':
#     unittest.main()
