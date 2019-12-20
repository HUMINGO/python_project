import requests
import json
from Config.read_config import read_config

#封装get请求，和post请求

class BaseRequest:
    '''
    发送get请求
    '''

    def send_get(self, url, data, cookie=None, get_cookie=None):
        res = requests.get(url=url, params=data, cookie=cookie)
        if get_cookie != None:
            res = res.cookies
        else:
            res = res.text
        return res

    def send_post(self, url, data, cookie=None, get_cookie=None):
        res = requests.post(url=url, data=data, cookie=cookie)
        if get_cookie != None:
            res = res.cookies
        else:
            res = res.text

        return res

    def run_main(self, method, url, data, cookie=None):

        base_url = read_config.get_http("host")
        url = base_url + url
        # print(url)
        if method == 'get':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res
        try:
            res = json.loads(res)
        except:
            print("这是一个test")
        return res


request = BaseRequest()
if __name__ == "__main__":
    request = BaseRequest()
    request.run_main("get", "/login", "{'username':111111}")