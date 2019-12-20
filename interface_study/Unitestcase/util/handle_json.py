#coding = utf-8

'''
获取到预期响应的数据
'''

import json
import os

base_url = os.getcwd()
print(base_url)

def read_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data

def get_value(key):
    data = read_json()
    return data[key]

def write_value(data):
    data_value = json.dumps(data)
    with open("/Users/my_home/PycharmProjects/interface_study/Config/cookie.json", "w") as f:
        f.write(data_value)


if __name__ == "__main__":
    data = {
        "app": {"cookie": "13481738"}
    }
    write_value(data)