import requests
import json


def login(url,data):
    res = requests.post(url=url, data=data)
    return json.dumps(res,indent=2,sort_keys=True)

# url = 'http://172.16.191.250/department/get_org_detail/?department_id=7'
url = 'http://172.16.191.250/'
data = {
    'csrfmiddlewaretoken': '2aDaXVdgM5m32H2AG25mEughUTSavWeN',
    'username':'admin',
    'password':'admin'
}




