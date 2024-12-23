import requests
from requests.auth import HTTPBasicAuth


def test():
    username = "wanyuan"
    password = "************"

    url = "https://11.22.33.44:49002/jenkins/job/基础服务/job/黔西南基础服务/job/ahcloud-etl/buildWithParameters"
    params = "origin/test/0331"
    params = {
        "branch": params,
    }
    headers = {
        "Content-Type": "application/json",  # 如果是发送 JSON 数据
    }
    requests.post(url=url, params=params, headers=headers, verify=False,auth=HTTPBasicAuth(username, password))

if __name__ == '__main__':
    test()