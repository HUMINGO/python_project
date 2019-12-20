import requests
import json
import hashlib


# url = "https://www.baidu.com"
# resqonse = requests.get(url,verify=False).text
# print(resqonse)

#下载文件
# down_url = "http://www.imooc.com/mobile/appdown"
# res = requests.get(down_url)
# with open("mukewang.apk","wb") as f:
#     f.write(res.content)

imooc = "imooc"
md5 = hashlib.md5()
md5.update(imooc.encode("utf-8"))
res = md5.hexdigest()
print(res)
