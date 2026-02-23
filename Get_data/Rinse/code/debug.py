# 作者：金石
# 创建时间：2023/6/26 17:04
# 文件名：debug.py
import csv

# 输入要插入的数据作为列表
data_to_insert = ["Catagory", "Title", "Authors","Subjects","Date"]
# 读取原始CSV文件内容
with open('../Clearout_all.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)
del rows[0]
# 在第一行之前插入新数据行
rows.insert(0, data_to_insert)

# 将更新后文件
with open('../Clearout_all.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
