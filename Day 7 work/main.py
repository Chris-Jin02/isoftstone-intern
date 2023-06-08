# 小组：01
# 作者：金石
# 创建时间：2023/6/8 11:10
# 文件名：main.py
from function import *
print('*'*50+'\n')
menu = {
    "1": {"info": "添加用户", "func": adduser},
    "2": {"info": "删除用户", "func": removeuser},
    "3": {"info": "修改用户", "func": updateuser},
    "4": {"info": "查询用户", "func": queryuser},
    "0": {"info": "退出程序", "func": exit}
}
while True:
    for k, v in menu.items():
        print(f"{k}. {v['info']}")
    choice = input("请选择操作：")
    if choice in menu:
        menu[choice]["func"]()
    else:
        print("未知选项，请重新选择")
    # 关闭连接
db_operation.close()
