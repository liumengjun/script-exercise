import xmltodict

def _wx_dict2xml(d):
    return xmltodict.unparse({'xml': d})


def _wx_xml2dict(xmlstr):
    return xmltodict.parse(xmlstr)['xml']


xml_string = '''
<xml>
   <return_code><![CDATA[SUCCESS]]></return_code>
   <return_msg><![CDATA[OK]]></return_msg>
   <appid><![CDATA[wx2421b1c4370ec43b]]></appid>
   <mch_id><![CDATA[10000100]]></mch_id>
   <nonce_str><![CDATA[IITRi8Iabbblz1Jc]]></nonce_str>
   <sign><![CDATA[7921E432F65EB8ED0CE9755F0E86D72F]]></sign>
   <result_code><![CDATA[SUCCESS]]></result_code>
   <prepay_id><![CDATA[wx201411101639507cbf6ffd8b0779950874]]></prepay_id>
   <trade_type><![CDATA[JSAPI]]></trade_type>
</xml>
'''
xml_dict = _wx_xml2dict(xml_string)
# print(xml_dict)
print(xml_dict['return_code']=='SUCCESS')
print(xml_dict['return_msg']=='OK')
print(xml_dict['appid']=='wx2421b1c4370ec43b')
print(xml_dict['mch_id']=='10000100')
print(xml_dict['nonce_str']=='IITRi8Iabbblz1Jc')
print(xml_dict['sign']=='7921E432F65EB8ED0CE9755F0E86D72F')
print(xml_dict['result_code']=='SUCCESS')
print(xml_dict['prepay_id']=='wx201411101639507cbf6ffd8b0779950874')
print(xml_dict['trade_type']=='JSAPI')

xml_string2 = _wx_dict2xml(xml_dict)
print(xml_string2)

xml_dict2 = _wx_xml2dict(xml_string)
print(xml_dict2)
print(xml_dict2['return_code']=='SUCCESS')
print(xml_dict2['return_msg']=='OK')
print(xml_dict2['appid']=='wx2421b1c4370ec43b')
print(xml_dict2['mch_id']=='10000100')
print(xml_dict2['nonce_str']=='IITRi8Iabbblz1Jc')
print(xml_dict2['sign']=='7921E432F65EB8ED0CE9755F0E86D72F')
print(xml_dict2['result_code']=='SUCCESS')
print(xml_dict2['prepay_id']=='wx201411101639507cbf6ffd8b0779950874')
print(xml_dict2['trade_type']=='JSAPI')
