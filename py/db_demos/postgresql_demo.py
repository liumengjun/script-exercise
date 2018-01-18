import psycopg2

database_cfg = {
    'database': 'maladb',
    'user': 'malauser',
    'password': 'mala123',
    'host': '127.0.0.1',
    'port': '5432',
}

# 数据库连接参数
conn = psycopg2.connect(**database_cfg)
cur = conn.cursor()
# cur.execute(
#     "CREATE TABLE test(id serial PRIMARY KEY, num integer,data varchar);")
# # insert one item
# cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (1, 'aaa'))
# cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (2, 'bbb'))
# cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (3, 'ccc'))

cur.execute("SELECT * FROM auth_user;")
rows = cur.fetchall()  # all rows in table
print(rows)
for i in rows:
    print(i)
conn.commit()
cur.close()
conn.close()
