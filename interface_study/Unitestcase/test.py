# -*- coding: utf-8 -*-

import requests
from base.base_requeses import request

def test():

    url = 'http://zhihuixiaoyuan-bjq-back-admin-8080.pubpaas.wasu.cn:41531/smartCampus_admin/login/doLogin'
    data = {
        "userName": "wasu_user1",
        "passwd": 111
    }

    res = request.run_main("GET", url, data)
    print(res)


if __name__ == "__main__":
    test()
