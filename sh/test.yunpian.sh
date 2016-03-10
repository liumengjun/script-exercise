#/bin/sh
#author jacky
#修改为您的apikey
apikey="$YUNPIAN_API_KEY"
echo $apikey
#修改为您要发送的手机号
mobile="18613888646"
#设置您要发送的内容
text="【云片网】您的验证码是1234"
echo "get user info:"
echo "http://yunpian.com/v1/user/get.json?apikey=$apikey"
curl "http://yunpian.com/v1/user/get.json?apikey=$apikey"
echo "\nsend sms:"
# curl --data "apikey=$apikey&mobile=$mobile&text=$text" "http://yunpian.com/v1/sms/send.json"

