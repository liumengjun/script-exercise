#!/usr/bin/python 
# -*- coding:utf-8 -*-
# coding=utf-8

#import mysql.connector, sys
import MySQLdb, sys

conn = MySQLdb.connect(host=sys.argv[1], user=sys.argv[2], passwd=sys.argv[3], db=sys.argv[4])
curs = conn.cursor()
#  查询表格  #
query = 'SELECT * FROM %s limit 100' % sys.argv[5]
print query
curs.execute(query)
# show result
for row in curs.fetchall():
	print row

# print 'end'