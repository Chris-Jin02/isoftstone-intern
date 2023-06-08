# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/7 16:47
# 文件名：mysql.py

import Package as mysql
def testQuery():
    sql = 'select * from users where username like (%s)'
    args = []
    # 一个参数
    # sql='select * from users where userid > %s'
    # args=[15] # 列表
    # 登录
    # sql='select * from users where username= %s and password=%s'
    # args=['ppp','ppp']
    query = input("请输入查询条数(整数)\n")
    temp = mysql.exe_query(sql, args, query)
    for t in temp:
        print(t)

def testUpdate():
    update = input("请输入修改类型: 1:添加, 2:修改, 3:删除, 0:返回菜单\n")
    if update == "1":
        sql = 'insert into users (username,password) values (%s,%s)'
        username = input("请输入用户名\n")
        password = input("请输入密码\n")
        args = [username, password]
    elif update == "2":
        # 修改
        sql = 'update users set username=%s where userid=%s'
        username = input("请输入用户名\n")
        password = input("请输入密码\n")
        args = [username, password]
    elif update == "3":
        # 删除
        userid = input("请输入用户id\n")
        sql = 'delete from users where userid=%s'
        args = [userid]
    elif update == "0":
        main()
    else:
        print("输入错误")
        testUpdate()
    num = mysql.exe_update(sql, args)
    print(num)

def main():
    type = input("请选择操作类型: 1:查询, 2:增删改, 0:结束代码\n")
    if type == "1":
        testQuery()
        main()
    elif type == "2":
        testUpdate()
        main()
    elif type == "0":
        return
    else:
        print("输入错误请重新输入\n")
        main()


if __name__ == '__main__':
    # testQuery()
    # testUpdate()
    main()
