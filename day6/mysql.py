# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/7 16:47
# 文件名：mysql.py

import Package as mysql
def testQuery():
    sql = 'select * from users'
    args = [] # 空列表
    # 一个参数
    # sql='select * from users where userid > %s'
    # args=[15] # 列表
    # 登录
    # sql='select * from users where username= %s and password=%s'
    # args=['ppp','ppp']
    temp = mysql.exe_query(sql, args, 5)
    for t in temp:
        print(t)

def testUpdate():
    update = input("请输入修改类型: 1:添加, 2:修改, 3:删除")
    if update == "1":
        sql = 'insert into users (username,password) values (%s,%s)'
        username = input("请输入用户名")
        password = input("请输入密码")
        args = [username, password]
    elif update == "2":
        # 修改
        sql = 'update users set username=%s where userid=%s'
        username = input("请输入用户名")
        password = input("请输入密码")
        args = [username, password]
    elif update == "3":
        # 删除
        sql = 'delete from users where userid=%s'
        userid = input("请输入用户id")
    num = mysql.exe_update(sql, args)
    print(num)

def main():
    type = input("请选择操作类型")
    if type == "1":
        testQuery()
    elif type == "2":
        testUpdate()


if __name__ == '__main__':
    # testQuery()
    # testUpdate()
    main()