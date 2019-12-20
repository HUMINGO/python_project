#coding=utf-8

import requests
import unittest
from base.base_requeses import request

url = "http://www.imooc,com"
data = {
    "username": 111111,
    "password": 222222
}

class Testcase01(unittest.TestCase):

    def setUp(self):
        print("case 开始执行")

    def tearDown(self):
        print("case 执行结束")

    @classmethod
    def setUpClass(cls):
        print("case类开始执行")

    @classmethod
    def tearDownClass(cls):
        print("case类执行结束")

    #运用最多的判断
    @unittest.skipIf(3>2, '这个case不执行')
    def test_01(self):
        print("case01")

    def test_02(self):
        print("case02")

    def test_04(self):
        print("case 04")


    def test_03(self):
        request.run_main('get', url, data)

if __name__ == "__main__":
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest((Testcase01("test_02")))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # tests = [Testcase01('test_04'), Testcase01('test_03'), Testcase01('test_01')]
    # suite.addTest(tests)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
