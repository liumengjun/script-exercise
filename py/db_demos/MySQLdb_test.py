#coding=gbk
#mysqldb    
import time, MySQLdb   
   
#����    
conn=MySQLdb.connect(host="localhost",user="root",passwd="lmj",db="test",charset="utf8")  
cursor = conn.cursor()    
   
#д��    
sql = "insert into test(name,address) values(%s,%s)"   
param = ("aaa",int(time.time()))    
n = cursor.execute(sql,param)    
print n    
   
#����    
sql = "update test set name=%s where id=3"   
param = ("bbb")    
n = cursor.execute(sql,param)    
print n    
   
#��ѯ    
n = cursor.execute("select * from test")    
for row in cursor.fetchall():    
    for r in row:    
        print r    
   
#ɾ��    
sql = "delete from test where name=%s"   
param =("aaa")    
n = cursor.execute(sql,param)    
print n    
cursor.close()    
   
#�ر�    
conn.close()