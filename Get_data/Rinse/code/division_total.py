# 作者：金石
# 创建时间：2023/6/28 14:32
# 文件名：division_total.py
import pandas as pd

# 读取CSV文件
df = pd.read_csv('../total.csv')

# 筛选出date为"2022-01"的行
filtered_df = df[df['date'] == '2023-06']

# 将筛选后的数据写入新的CSV文件
filtered_df.to_csv('../division_csv/2023-06.csv', index=False)