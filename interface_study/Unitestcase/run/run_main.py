import unittest
import os
from Unitestcase.util.handle_excel import excel_data
from Unitestcase.util.handle_json import get_value
from base.base_requeses import request
from Unitestcase.handle_result import handle_result, get_res_json
from Unitestcase.util.handle_cookies import get_cookie_value, write_cookie


class Runmain():

    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            cookie = None
            data = excel_data.get_rows_value(i+2)
            is_run = data[2]
            if is_run == "yes":
                method = data[4]
                url = "http://zhihuixiaoyuan-zhxy-back-test-8080.pubpaas.wasu.cn:41535/SMSCH-ADMIN"+data[5]
                data1 = data[6]
                expect_method = data[8]

                message = res["message"]
                expect_result = res['code']
                cookie_method = data[10]
                if cookie_method == "yes":
                    cookie = get_cookie_value("path", "web")
                res = request.run_main(method, url, data1, cookie=cookie)

                if cookie_method == "write":
                    write_cookie(data, "app", "path")


                #不同的预期方式采用不同的判断
                if expect_method == "message":
                    config_message = get_value('message')
                    if message == config_message:
                        print("case通过")
                        excel_data.excel_write_data(i+2, 11, "pass")
                    else:
                        print("case失败")
                        excel_data.excel_write_data(i+2, 11, "fail")
                        excel_data.excel_write_data(i+2, 12, res)

                if expect_method == "errorcode":
                    code = get_value("code")
                    if expect_result == code:
                        print("case通过")
                        excel_data.excel_write_data(i+2, 11, "pass")
                    else:
                        print("case失败")
                        excel_data.excel_write_data(i + 2, 11, "fail")
                        excel_data.excel_write_data(i + 2, 12, res)

                if expect_method == "json":
                    if code == 10000:
                        status_str = "success"
                    else:
                        status_str = "error"
                    result = get_res_json("www.baidu.com", status_str)
                    test_res = handle_result(res, result)
                    if test_res:
                        print('case执行成功')
                        excel_data.excel_write_data(i+2, 11, "pass")
                    else:
                        print('case执行失败')
                        excel_data.excel_write_data(i + 2, 11, "fail")
                        excel_data.excel_write_data(i + 2, 12, res)



if __name__ == "__main__":
    run_main = Runmain()
    run_main.run_case()