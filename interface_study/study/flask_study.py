
# -*- coding: utf-8 -*-

from flask import Flask,request
import json

app = Flask(__name__)

@app.route("/login",methods=["GET"])
def login():

    username = request.args.get("username")
    password = request.args.get("password")
    if username and password:
        data = json.dumps({
            "username":username,
            "password":password,
            "code":200,
            "msg":"登陆成功"
        },ensure_ascii=False)
        
    else:
        data = json.dumps(
            {
                "msg":"传递参数为空"
            },ensure_ascii=False
        )
    return data

@app.route("/post_login",methods=["POST"]
def post_login():

    request_method = request.method
    if request_method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        data = json.dumps({
            "username":username,
            "password":password,
            "code":200,
            "msg":"登陆成功"
        },ensure_ascii=False)
    else:
        data = json.dumps(
            {
                "msg":"传递参数为空"
            },ensure_ascii=False
        )
    return data


if __name__ == "__main__":
    app.run()