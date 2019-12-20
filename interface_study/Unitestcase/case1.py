from base.base_requeses import request
import unittest
import json
from unittest import mock
import os
import requests
# from HTMLTestRunner import HTMLTestRunner
import HTMLTestRunner
url = 'http://zhihuixiaoyuan-zhxy-back-test-8080.pubpaas.wasu.cn:41535/SMSCH-ADMIN/port/admin/login'
data = {
    "username": "ceshi03",
    "password": 123456
}

path = os.getcwd()


def read_json():
    with open(path + "/user_data.json") as f:
        data1 = json.load(f)
        return data1


class Testcase(unittest.TestCase):

    def setUpClass(cls) -> None:
        print('测试开始执行')

    def tearDownClass(cls) -> None:
        print('测试执行结束')

    def test_01(self):
        mock_method = mock.Mock(return_value=read_json())
        request.run_main = mock_method
        res1 = request.run_main("post", url=url, data=data)
        self.assertEqual(res1["errorcode"], 1001)

    def test_02(self):

        res = requests.get(url=url, params=data).json()
        self.assertEqual(res["errorcode"], 1001)



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Testcase("test_02"))
    suite.addTest(Testcase("test_01"))
    # file_path = path + "/report/test_report.html"
    # with open(file_path, "wb") as f:
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="this is a test", description="humin")
    # print(file_path)
    fp = open('/Users/my_home/Desktop/b.html', 'wb')  # 定义测试报告存放路径
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='百度搜索测试报告', description='用例执行情况')  # 定义测试报告
    runner.run(suite)  # 执行测试用例
    fp.close()

