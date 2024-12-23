import logging

import requests
from flask import Flask, jsonify, request, render_template
from requests.auth import HTTPBasicAuth
import sys


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-python-script', methods=['GET'])
def run_python_script():
    # try:
        # 从查询参数中获取参数
        apiUrl = request.args.get('apiUrl')
        branch = request.args.get('branch')
        print("部署地址为：", apiUrl, "分支为：", branch)
        username = "wanyuan"
        password = "************"
        url = apiUrl
        branch = branch
        data = {
            "branch":branch,
        }
        headers = {
            "Content-Type": "application/json",
        }# -*- coding: utf-8 -*-
        print("data数据",data)
        requests.post(url=url, data=data, headers=headers, verify=False, auth=HTTPBasicAuth(username, password))
        return jsonify({'message': '开始调用部署API', 'url': apiUrl, 'branch': branch}), 200

#     else:
    #         return jsonify({'message': '脚本执行失败', 'error': result.stderr}), 500
    #     except Exception as e:
    #         return jsonify({'message': '执行脚本时出错', 'error': str(e)}), 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
