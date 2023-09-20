from django.test import TestCase
import unittest
import requests


# Create your tests here.
class HTTPUnitTesting(unittest.TestCase):

    # Test if end-point returns correct count
    def test_get_node(self):
        result = requests.get('http://127.0.0.1:8000/node/').json()
        self.assertEqual(len(result), 4)

    # Test if end-point post data
    def test_create_node(self):
        data = {
            "name": "surveillance-8",
            "x_position": 700,
            "y_position": 700,
            "date_created": 1690826356,
            "date_updated": 1690826356
        }
        result = requests.get('http://127.0.0.1:8000/node/',data=data).json()
        self.assertIsNotNone(result, "Result Success")

    # Test if end-point post data
    def test_get_partner(self):
        result = requests.post('http://127.0.0.1:8000/partner/').json()
        self.assertGreaterEqual(len(result), 0)

    # Test if end-point post data
    def test_create_partner(self):
        data = {
            "from_person": 3,
            "to_person": 2,
            "angle_start": 90,
            "angle_end": 270,
            "date_created": 1690826356,
            "date_updated": 1690826356
        }
        result = requests.post('http://127.0.0.1:8000/partner/', data=data).json()
        self.assertIsNotNone(result, "Result Success")

    # Test if end-point post data
    def test_generate_report(self):
        data = {
            'name': "",
            'timestamp': "",
            'frame_count': "",
            'model_id': ""
        }
        result = requests.post('http://127.0.0.1:8000/report/', data=data).json()
        return self.assertIsNotNone(result,'Report Received')


def suite():
    """
        Gather all the tests and deploy in suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(HTTPUnitTesting))
    return test_suite


if __name__ == '__main__':
    test_suit = suite()
    runner = unittest.TextTestRunner()
    runner.run(test_suit)
