# 使用requests.Session登录，然后代用其他的API，随机添加规则

import json
import requests

username = 'admin'
password = 'admin'

host_url = 'http://localhost:9600'


def login(session):
    session.post(host_url + '/login/auth',
                 data={'username': username, 'password': password})


def list_item_by_unit_id(session, du_id):
    resp = session.get(host_url + '/units/%d/items' % du_id)
    # print(resp.text)
    item_list = json.loads(resp.text)['data']
    return [rs['id'] for rs in item_list]


def demo(du_id):
    session = requests.Session()
    login(session)
    rs_ids = list_item_by_unit_id(session, du_id)
    print(rs_ids)
    print('end')


if __name__ == '__main__':
    demo(21)
