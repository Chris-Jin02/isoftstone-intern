# 作者：金石
# 创建时间：2023/6/28 10:55
# 文件名：total_rewrite_csv.py
import pandas as pd
from datetime import timedelta, date
import numpy as np

#读取csv文件
df = pd.read_csv('../total_csv/Download_total_astro-ph.csv')

#生成date序列
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

start_date = '2022-01'
end_date = '2023-06'
date_range = pd.period_range(start=start_date, end=end_date, freq='M')
#在第一列前加入新列，数据长度不足的填补为NaN
df.insert(0, 'date', date_range)

#在最后加入一列，列名为subject，数据以0填充
df["subject"] = np.array(len(df))
df["subject"] = "astro-ph"

#存储CSV文件
df.to_csv('../total_rewrite_csv/astro-ph_total.csv',index=False)
