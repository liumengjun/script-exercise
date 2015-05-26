#-*- coding: utf-8 -*-  
#coding=utf-8  
from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

config = {
  'user': 'root',
  'password': 'lmj',
  'host': '127.0.0.1',
  'database': 'test',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

now = datetime.now()
today = now.date()
tomorrow = today + timedelta(days=1)

print( today )
print( tomorrow )
now_str = now.strftime("%Y-%m-%d %H:%M:%S")
print( now_str )

# desc是mysql关键字，直接写可能导致sql解析出错 
add_test = ("INSERT INTO test "
               "(`name`, `address`, `desc`) "
               "VALUES (%s, %s, %s)")

data_employee = ('Geert', 'China', 'added by python @' + now_str)

# Insert new employee
cursor.execute(add_test, data_employee)
emp_no = cursor.lastrowid
print( emp_no )

# Make sure data is committed to the database
cnx.commit()


n = cursor.execute("select * from test")    
for row in cursor.fetchall():    
    for r in row:    
        print( r )

cursor.close()


cnx.close()