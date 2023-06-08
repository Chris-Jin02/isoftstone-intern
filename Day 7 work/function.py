# 小组：01
# 作者：金石
# 创建时间：2023/6/8 11:11
# 文件名：function.py
from mysql import UserDBOperation
db_operation = UserDBOperation()
def adduser():
    # 添加用户
    username = input("请输入用户名：")
    password = input("请输入密码：")
    db_operation.add_user(username, password)


def queryuser():
    # 查询用户
    userid = input("请输入要查询的用户ID：")
    db_operation.query_user_by_id(userid)


def removeuser():
    # 删除用户
    userid = input("请输入要删除的用户ID：")
    db_operation.remove_user_by_id(userid)


def updateuser():
    # 更新用户信息
    userid = input("请输入要更新的用户ID：")
    new_username = input("请输入新的用户名：")
    new_password = input("请输入新的密码：")
    db_operation.update_user_by_id(userid, new_username, new_password)