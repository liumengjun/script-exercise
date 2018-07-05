#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import datetime
import getpass
import sys
import mysql.connector

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', help='db user, default login user')
parser.add_argument('--host', help='db host, default "127.0.0.1"')
parser.add_argument('-d', '--dbname', help='db name, default `test_db`')
parser.add_argument('-b', '--business_name', required=True, help='必须。业务线名称')
parser.add_argument('--admin',  required=True, help='必须。管理员用户名')
# print(sys.argv)
args, _ = parser.parse_known_args(sys.argv[1:])
# print(args)

dbuser = args.user or getpass.getuser()
password = getpass.getpass('db password:')
host = args.host or '127.0.0.1'
dbname = args.dbname or 'test_db'
config = {
    'user': dbuser,
    'password': password,
    'host': host,
    'database': dbname,
    'raise_on_warnings': True,
}

business_name = args.business_name
admin_username = args.admin
business_description = business_name + '业务线'
now = datetime.datetime.now()
current_time_millis = int(now.timestamp() * 1000)

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

exists = 0
cursor.execute("select count(*) from business_user where username='%s'" %
               admin_username)
for (count, ) in cursor:
    exists = count
if exists:
    print('用户 %s 已存在' % admin_username)
    exit()

######################
# other db ops
######################


# Make sure data is committed to the database
cnx.commit()

cursor.close()

cnx.close()

print('create business %s and user %s finished' % (business_name, admin_username))
