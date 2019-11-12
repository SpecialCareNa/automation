#coding=utf8
import requests
import json
from util.handle_init import handle_ini

import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)


class RunMain:



    def send_post(self,url,data):
        cookies = 'sessionid=w017z2zx06a5i9vskuku4f5siwo62dbm'
        cookies2 = dict(map(lambda x: x.split('='), cookies.split(";")))
        res = requests.post(url=url, data=data, cookies=cookies2)
        # print(res.json()['data']['data'][0])
        return json.loads(res.content)
        # return res
        # json_res = res.json()
        # print(json.dumps(json_res,indent=2,ensure_ascii=False))

    def send_get(self,url,data):
        cookies = 'sessionid=w017z2zx06a5i9vskuku4f5siwo62dbm'
        cookies2 = dict(map(lambda x: x.split('='), cookies.split(";")))
        res = requests.get(url=url, data=data, cookies=cookies2)
        print(res.content)
        return json.loads(res.content)
        # return res

    def run_main(self,url,method,data=None):
        # print("传递的值"+url)
        base_url = handle_ini.get_value("host")
        # print("配置文件host的值"+base_url)
        if 'http' not in url:
            url = base_url + url

        self.res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        # try:
        #     res = json.loads(res)
        # except:
        #     print("1是text")
        return res

request = RunMain()

if __name__ == '__main__':

    url = 'opscenter/script/script_page/'
    aaa = json.dumps({'para': {'page': 1, 'per_page': 10}})
    data = {"json": aaa}
    run = RunMain()
    print(run.run_main(url,'POST',data))





