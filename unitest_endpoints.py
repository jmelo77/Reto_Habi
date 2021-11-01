from unittest import TestCase
from app import app
from flask import json

class TestEndpoints(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
        self.testapp = app.test_client()

    def tearDown(self):
        pass

    def test_list_properties(self):
        res = self.testapp.post('http://127.0.0.1:5000/habi-api/api/v1/prop/fil', data=json.dumps({
              'status': 'pre_venta',
              'year': 2020,
              'city': 'bogota'}), headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
              follow_redirects=True)
        self.assertEqual(res.status_code, 200)    

    def test_health(self):
        res = self.testapp.get('http://127.0.0.1:5000/habi-api/api/v1/health',
                    headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
                    follow_redirects=True)
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    TestCase.main()             