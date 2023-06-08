# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/7 16:38
# 文件名：Package.py

import pymysql

def getCon():
    con = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='test')
    cursor = con.cursor()
    return con, cursor

def closeAll(con, cursor):
    cursor.close()
    con.close()

def exe_update(sql, args):
    con, cursor = getCon()
    num = cursor.execute(sql, args)
    con.commit()
    closeAll(con, cursor)
    return num

def exe_query(sql, args, num): # num 为几条数据
    con, cursor = getCon()
    cursor.execute(sql, args)
    # if num == 1:temp=cursor.fetchone() #此方法没有意义
    if num == all:
        temp = cursor.fetchall()
    else:
        num = int(num)
        if num > 0:
            temp = cursor.fetchmany(int(num))
        else:
            print("请输入大于0的数")
    con.commit()
    closeAll(con, cursor)
    return temp

