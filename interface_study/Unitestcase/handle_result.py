import json
from Unitestcase.util.handle_json import get_value
from deepdiff import DeepDiff

'''
处理响应结果，获取到预期的响应结果
'''
#比较两个字典的变化

def handle_result(dict1, dict2):
    # dict1={
    #     "aa": "111",
    #     "bbgg": "222"
    # }
    #
    # dict2={
    #     "aa": "111",
    #     "bb": "222"
    # }
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        comp_dict = DeepDiff(dict1, dict2, ingnore_order=True).to_dict()
        if comp_dict.get("dictionary_item_added"):
            print("case失败")
        else:
            print("cast成功")

def get_res_json(url, status):
    data = get_value(key=url)
    if data != None:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None



