import unittest
from unittest import mock
import requests

url = "http://www.imooc.com/login"
data = {
    "username":"111111",
    "password":"11112"
}

def post_request(url,data):
    res = requests.post(url,data).json()
    return res

def get_request(url,data):
    res = requests.get(url,data).json()
    return res

class TestLogin(unittest.TestCase):

    def setUp(self):
        print("test开始")

    def tearDown(self):
        print("test结束")

    def test_01(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username":"111111"
        }
        success_test = mock.Mock(return_value=data)
        post_request = success_test

        res = post_request
        self.assertEqual("111222", res())

if __name__ == "__main__":
    unittest.main()






