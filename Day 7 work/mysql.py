# 小组：01
# 作者：金石
# 创建时间：2023/6/8 11:11
# 文件名：mysql.py
import pymysql
class UserDBOperation:
    def __init__(self, host='localhost', port=3306, user='root', password='jinshi1234', database='test'):
        self.con = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def add_user(self, username, password,):
        sql = 'insert into users(userid,username,password) values (%s,%s,%s)'
        self.cursor.execute('SELECT * FROM users ORDER BY userID DESC LIMIT 1')
        Index = self.cursor.fetchone()
        Index = int(Index[0])
        args = [Index+1, username, password]
        try:
            self.cursor.execute(sql, args)
            self.con.commit()
            print('数据添加成功')
        except Exception as e:
            print(f"添加数据失败，错误信息为：{e}")

    def query_user_by_id(self, user_id):
        sql = 'select * from users where userid=%s'
        args = [user_id]
        try:
            self.cursor.execute(sql, args)
            user = self.cursor.fetchone()
            print(user)
        except Exception as e:
            print(f"查询数据失败，错误信息为：{e}")

    def remove_user_by_id(self, user_id):
        sql = 'delete from users where userid=%s'
        args = [user_id]
        try:
            self.cursor.execute(sql, args)
            self.con.commit()
            print('数据删除成功')
        except Exception as e:
            print(f"删除数据失败，错误信息为：{e}")

    def update_user_by_id(self, user_id, new_username, new_password):
        sql1 = 'update users set username=%s where userid=%s'
        sql2 = 'update users set password=%s where userid=%s'
        args1 = [new_username, user_id]
        args2 = [new_password, user_id]
        try:
            self.cursor.execute(sql1, args1)
            self.cursor.execute(sql2, args2)
            self.con.commit()
            print('数据更新成功')
        except Exception as e:
            print(f"更新数据失败，错误信息为：{e}")