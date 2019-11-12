import requests
import json


class RunMain:
    def __init__(self, url, method, data=None):
        self.res = self.run_main(url, method, data)

    def send_post(self, url, data):
        cookies = 'csrftoken=0fR1kvu478l1z7Alstp0QO6atYZYkkrK; sessionid=so61wu7azdbc0p26oi4fsqpkspnl3rxj'
        cookies2 = dict(map(lambda x: x.split('='), cookies.split(";")))
        res = requests.post(url=url, data=data, cookies=cookies2)
        print(res.content)
        return json.loads(res.content)

    def send_get(self, url, data):
        cookies = 'csrftoken=0fR1kvu478l1z7Alstp0QO6atYZYkkrK; sessionid=so61wu7azdbc0p26oi4fsqpkspnl3rxj'
        cookies2 = dict(map(lambda x: x.split('='), cookies.split(";")))
        res = requests.get(url=url, data=data, cookies=cookies2)
        print(res.content)
        return json.loads(res.content)

    def run_main(self, url, data=None, method=None):
        res = None
        if method == 'GET':
            res = self.send_get()
        else:
            res = self.send_post()
        return res


if __name__ == '__main__':
    url = ''
    data = {

    }

    run = RunMain(url, data, 'GET')
    print(run.res)
    # print(run.run_main(url,data,'GET'))