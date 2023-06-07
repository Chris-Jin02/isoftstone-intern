# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/7 16:01
# 文件名：query.py

import pymysql
# 获取数据库连接
con = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='test', charset='utf8')
# 获取游标
cursor = con.cursor()
# 定义 sql
sql = 'select * from users'
# sql = 'select * from users where username> %s'
# args = ['']
# 执行 sql
cursor.execute(sql)
# 获取了一条数据，后面获取所有也不会有第一条数据了，因为游标已经下移了
# one = cursor.fetchone()
# print(one)
print('*' * 50)
users = cursor.fetchmany(5)
for user in users:
    print(user)
print('*' * 50)
# users = cursor.fetchall()
# for user in users:
# print(user)
# 提交数据
con.commit()
# 关闭 cursor 对象
cursor.close()
# 关闭 con 对象
con.close()