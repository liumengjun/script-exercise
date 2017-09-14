
import time
import random
import json
from pprint import pprint
import requests

moneys = [
    {'code': 'AED', 'idx': 'A', 'name': '阿联酋迪拉姆'},
    {'code': 'AUD', 'idx': 'A', 'name': '澳元'},
    {'code': 'MOP', 'idx': 'A', 'name': '澳门元'},
    {'code': 'DZD', 'idx': 'A', 'name': '阿尔及利亚第纳尔'},
    {'code': 'OMR', 'idx': 'A', 'name': '阿曼里亚尔'},
    {'code': 'EGP', 'idx': 'A', 'name': '埃及镑'},
    {'code': 'BYR', 'idx': 'B', 'name': '白俄罗斯卢布'},
    {'code': 'BRL', 'idx': 'B', 'name': '巴西雷亚尔'},
    {'code': 'PLN', 'idx': 'B', 'name': '波兰兹罗提'},
    {'code': 'BHD', 'idx': 'B', 'name': '巴林第纳尔'},
    {'code': 'BGN', 'idx': 'B', 'name': '保加利亚列弗'},
    {'code': 'ISK', 'idx': 'B', 'name': '冰岛克朗'},
    {'code': 'DKK', 'idx': 'D', 'name': '丹麦克朗'},
    {'code': 'RUB', 'idx': 'E', 'name': '俄罗斯卢布'},
    {'code': 'PHP', 'idx': 'F', 'name': '菲律宾比索'},
    {'code': 'HKD', 'idx': 'G', 'name': '港元'},
    {'code': 'COP', 'idx': 'G', 'name': '哥伦比亚比索'},
    {'code': 'CRC', 'idx': 'G', 'name': '哥斯达黎加科朗'},
    {'code': 'KRW', 'idx': 'H', 'name': '韩元'},
    {'code': 'CAD', 'idx': 'J', 'name': '加元'},
    {'code': 'CZK', 'idx': 'J', 'name': '捷克克朗'},
    {'code': 'KHR', 'idx': 'J', 'name': '柬埔寨瑞尔'},
    {'code': 'HRK', 'idx': 'K', 'name': '克罗地亚库纳'},
    {'code': 'QAR', 'idx': 'K', 'name': '卡塔尔里亚尔'},
    {'code': 'KWD', 'idx': 'K', 'name': '科威特第纳尔'},
    {'code': 'KES', 'idx': 'K', 'name': '肯尼亚先令'},
    {'code': 'LAK', 'idx': 'L', 'name': '老挝基普'},
    {'code': 'RON', 'idx': 'L', 'name': '罗马尼亚列伊'},
    {'code': 'LBP', 'idx': 'L', 'name': '黎巴嫩镑'},
    {'code': 'CNH', 'idx': 'L', 'name': '离岸人民币'},
    {'code': 'USD', 'idx': 'M', 'name': '美元'},
    {'code': 'BUK', 'idx': 'M', 'name': '缅甸元'},
    {'code': 'MYR', 'idx': 'M', 'name': '马来西亚林吉特'},
    {'code': 'MAD', 'idx': 'M', 'name': '摩洛哥道拉姆'},
    {'code': 'MXN', 'idx': 'M', 'name': '墨西哥元'},
    {'code': 'NOK', 'idx': 'N', 'name': '挪威克朗'},
    {'code': 'ZAR', 'idx': 'N', 'name': '南非兰特'},
    {'code': 'EUR', 'idx': 'O', 'name': '欧元'},
    {'code': 'CNY', 'idx': 'R', 'name': '人民币'},
    {'code': 'CHF', 'idx': 'R', 'name': '瑞士法郎'},
    {'code': 'JPY', 'idx': 'R', 'name': '日元'},
    {'code': 'SEK', 'idx': 'R', 'name': '瑞典克朗'},
    {'code': 'SAR', 'idx': 'S', 'name': '沙特里亚尔'},
    {'code': 'LKR', 'idx': 'S', 'name': '斯里兰卡卢比'},
    {'code': 'RSD', 'idx': 'S', 'name': '塞尔维亚第纳尔'},
    {'code': 'THB', 'idx': 'T', 'name': '泰铢'},
    {'code': 'TZS', 'idx': 'T', 'name': '坦桑尼亚先令'},
    {'code': 'BND', 'idx': 'W', 'name': '文莱元'},
    {'code': 'UGX', 'idx': 'W', 'name': '乌干达先令'},
    {'code': 'ZMK', 'idx': 'X', 'name': '新的赞比亚克瓦查'},
    {'code': 'SYP', 'idx': 'X', 'name': '叙利亚镑'},
    {'code': 'NZD', 'idx': 'X', 'name': '新西兰元'},
    {'code': 'TRY', 'idx': 'X', 'name': '新土耳其里拉'},
    {'code': 'SGD', 'idx': 'X', 'name': '新加坡元'},
    {'code': 'TWD', 'idx': 'X', 'name': '新台币'},
    {'code': 'HUF', 'idx': 'X', 'name': '匈牙利福林'},
    {'code': 'GBP', 'idx': 'Y', 'name': '英镑'},
    {'code': 'JOD', 'idx': 'Y', 'name': '约旦第纳尔'},
    {'code': 'IQD', 'idx': 'Y', 'name': '伊拉克第纳尔'},
    {'code': 'VND', 'idx': 'Y', 'name': '越南盾'},
    {'code': 'ILS', 'idx': 'Y', 'name': '以色列新锡克尔'},
    {'code': 'INR', 'idx': 'Y', 'name': '印度卢比'},
    {'code': 'IDR', 'idx': 'Y', 'name': '印尼卢比'},
    {'code': 'CLP', 'idx': 'Z', 'name': '智利比索'}
]
print(len(moneys))

# 收集 汇率列表
rate_list = []
# cb = 'jQuery11020146337876586067_%d' % int(time.time() * 1000)
params = {
    'query': '1人民币等于多少马来西亚林吉特',
    'co': '',
    'resource_id': 6017,
    't': int(time.time() * 1000),
    'cardId': 6017,
    'ie': 'utf8',
    'oe': 'gbk',
    'cb': 'op_aladdin_callback',
    'format': 'json',
    'tn': 'baidu',
    'cb': '',
    '_': int(time.time() * 1000)
}
api_url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php'

for money in moneys:
    if '人民币' == money['name']:
        continue
    params['query'] = '1人民币等于多少%s' % money['name']
    resp = requests.get(api_url, params=params)
    parsed = json.loads(resp.text)
    data0 = parsed['data'][0]
    rate_list.append({'rate': data0['number2'], 'name': data0['currency2']})
    # print(json.dumps(parsed, indent=4, ensure_ascii=False, sort_keys=True))
    # pprint(parsed)
    print('%s  <->  %s' % (data0['content1'], data0['content2']))
    time.sleep(1 + random.random())

# moneys 数组来源
# tab = parsed['data'][0]['tab'][1:]
# moneys = []
# for item in tab:
#     moneys.extend(item['moneys']['money'])
# pprint(moneys)


rate_list.sort(key=lambda x: float(x['rate']))
print('汇率列表@%s' % time.ctime())
pprint(rate_list)

# 汇率列表@Thu Sep 14 21:50:45 2017
[
    {'name': '科威特第纳尔', 'rate': '0.04596'},
    {'name': '巴林第纳尔', 'rate': '0.05753'},
    {'name': '阿曼里亚尔', 'rate': '0.05869'},
    {'name': '约旦第纳尔', 'rate': '0.1081'},
    {'name': '英镑', 'rate': '0.1142'},
    {'name': '欧元', 'rate': '0.1284'},
    {'name': '瑞士法郎', 'rate': '0.1475'},
    {'name': '美元', 'rate': '0.1526'},
    {'name': '加元', 'rate': '0.1863'},
    {'name': '澳元', 'rate': '0.1917'},
    {'name': '文莱元', 'rate': '0.2061'},
    {'name': '新加坡元', 'rate': '0.2061'},
    {'name': '新西兰元', 'rate': '0.2119'},
    {'name': '保加利亚列弗', 'rate': '0.2512'},
    {'name': '白俄罗斯卢布', 'rate': '0.2965'},
    {'name': '巴西雷亚尔', 'rate': '0.4794'},
    {'name': '新土耳其里拉', 'rate': '0.5278'},
    {'name': '以色列新锡克尔', 'rate': '0.5396'},
    {'name': '波兰兹罗提', 'rate': '0.5504'},
    {'name': '卡塔尔里亚尔', 'rate': '0.5553'},
    {'name': '阿联酋迪拉姆', 'rate': '0.5603'},
    {'name': '沙特里亚尔', 'rate': '0.5721'},
    {'name': '罗马尼亚列伊', 'rate': '0.591'},
    {'name': '马来西亚林吉特', 'rate': '0.6414'},
    {'name': '丹麦克朗', 'rate': '0.9557'},
    {'name': '克罗地亚库纳', 'rate': '0.9612'},
    {'name': '离岸人民币', 'rate': '1.0017'},
    {'name': '港元', 'rate': '1.1918'},
    {'name': '挪威克朗', 'rate': '1.209'},
    {'name': '埃及磅', 'rate': '1.2107'},
    {'name': '澳门元', 'rate': '1.2262'},
    {'name': '瑞典克朗', 'rate': '1.2262'},
    {'name': '摩洛哥道拉姆', 'rate': '1.4329'},
    {'name': '新的赞比亚克瓦查', 'rate': '1.4439'},
    {'name': '南非兰特', 'rate': '2.0129'},
    {'name': '墨西哥元', 'rate': '2.7128'},
    {'name': '捷克克朗', 'rate': '3.3524'},
    {'name': '新台币', 'rate': '4.6021'},
    {'name': '泰铢', 'rate': '5.0526'},
    {'name': '菲律宾比索', 'rate': '7.84'},
    {'name': '俄罗斯卢布', 'rate': '8.8056'},
    {'name': '印度卢比', 'rate': '9.7818'},
    {'name': '塞尔维亚第纳尔', 'rate': '15.2433'},
    {'name': '肯尼亚先令', 'rate': '15.6827'},
    {'name': '冰岛克朗', 'rate': '16.1998'},
    {'name': '日元', 'rate': '16.8757'},
    {'name': '阿尔及利亚第纳尔', 'rate': '16.9853'},
    {'name': '斯里兰卡卢比', 'rate': '23.3181'},
    {'name': '匈牙利福林', 'rate': '39.5652'},
    {'name': '叙利亚镑', 'rate': '78.566'},
    {'name': '哥斯达黎加科朗', 'rate': '87.7086'},
    {'name': '智利比索', 'rate': '95.7468'},
    {'name': '韩元', 'rate': '173.0847'},
    {'name': '伊拉克第纳尔', 'rate': '177.8795'},
    {'name': '缅甸元', 'rate': '206.5599'},
    {'name': '黎巴嫩镑', 'rate': '229.672'},
    {'name': '坦桑尼亚先令', 'rate': '341.4188'},
    {'name': '哥伦比亚比索', 'rate': '444.2288'},
    {'name': '乌干达先令', 'rate': '548.4363'},
    {'name': '柬埔寨瑞尔', 'rate': '616.476'},
    {'name': '老挝基普', 'rate': '1266.209'},
    {'name': '印尼卢比', 'rate': '2021.2052'},
    {'name': '越南盾', 'rate': '3466.9718'}
]
