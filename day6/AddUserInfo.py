# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/7 14:41
# 文件名：AddUserInfo.py

import pymysql

# 获取数据库连接
con = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='test')

# 获取游标
cursor = con.cursor()

# 定义 sql
sql = 'insert into users (username,password) values (%s,%s)'

# 输入
username = input("请输入用户名")
password = input("请输入密码")

# sql 的参数
args = [username, password]
# 列表

# 执行 sql
num = cursor.execute(sql, args)
print(str(num) + ' 条数据被添加')

# 提交数据
con.commit()

# 关闭 cursor 对象
cursor.close()

# 关闭 con 对象
con.close()
