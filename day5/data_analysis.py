# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/5 10:14
# 文件名：data_analysis.py

import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv('./新冠最新数据.csv', encoding='gbk')

# 排除城市里为空的
df = df[['province', 'confirmed']][df['city'].notnull()]

# 按省份分组求和并按 confirmed 降序排列,Ture 就为升序排列
df = df.groupby('province').sum().sort_values(by='confirmed',ascending=False)
# print(df)

df = df.iloc[0:10]
# 简化写法
df.insert(0, 'id', range(1, len(df)+1))
# print(df)

df = df.reset_index(drop = False) #放弃原来的索引
df=df.set_index('id') #将 id 列设置为新的索引
print(df)
df.to_csv('./十大省份确诊人数.csv',encoding='gbk')
