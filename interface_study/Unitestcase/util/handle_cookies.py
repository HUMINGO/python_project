#coding=utf-8

'''
操作cookies
1、获取cookie；
2、写入cookie；
3、携带cookie；
'''
import os
import sys
import json
from Unitestcase.util.handle_json import get_value, read_json, write_value

'''
从接口返回中获取到cookie
'''
def get_cookie_value(file_path, cookie_key):
    #获取到cookie
    # data1 = {"aaa": "bbb1"}
    data = read_json(file_path)
    return data[cookie_key]
    # data["app"] = data1
    # write_value(data)

def write_cookie(data, cookie_key,file_path):
    #写入cookie
    data = read_json(file_path=file_path)
    data[cookie_key] = data
    write_value(data=data)



if __name__ == "__main__":
    file = "/Users/my_home/PycharmProjects/interface_study/Config/cookie.json"
    get_cookie_value(file_path=file)