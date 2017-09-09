#!/usr/bin/env python
import json
import random
import concurrent.futures
import requests
import time
import uuid
import sys

print(sys.argv)
if len(sys.argv) < 2:
    print("please give ENV argument. (local, dev|test, or host-ip)")
    exit()
env = test_host = sys.argv[1]
if env == 'local':
    test_host = 'localhost'
elif env == 'test' or env == 'dev':
    test_host = '192.168.1.5'
else:
    pass  # IGNORE

host = 'http://' + test_host + ':23333'
#host = 'http://localhost:23333'
api_url = host + '/api/v1/callRule'

# 整理用户ID
uid_list = []
with open('baseInfoIdList.json') as fp:
    uid_list = json.load(fp)
print(len(uid_list))

random.shuffle(uid_list)
total = len(uid_list)

# 可选事件类型列表
event_type_list = ['NOT_EXISTS', '登录', '填写申请表', '填写绑定手机',
                   '绑定银行卡', '提交申请表', '提款', '提额申请', '更改绑定手机号或银行卡']

# 计时
start_time = time.time()


def run(userId, i):
    # time.sleep(1)
    event_type = random.choice(event_type_list)
    # print(userId)
    if (i % 10 == 0):
        print(('[%d]:%0.2f%% time=%0.1fs' %
               (i, i / total, time.time() - start_time)).center(80, '-'))

    params = {
        'transactionId': str(uuid.uuid4().hex),
        'uid': userId,
        'event': event_type
    }
    try:
        resp = requests.post(api_url, data=params, timeout=10)
        resp_str = resp.content.decode('utf-8')
        print('%s -> %s' % (userId, resp_str))
    except Exception as err:
        print("Error: " + str(err))


with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
    # with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    for i, uid in enumerate(uid_list):
        executor.submit(run, uid, i)
