# 小组：01
# 作者：金石
# 创建时间：2023/6/22 17:49
# 文件名：Cleanout_csv.py
import pandas as pd

# 读取CSV文件并创建DataFrame对象
df = pd.read_csv('../Merge/Merge_data/merge_2022.csv')

# 去除重复的标题行
df.drop_duplicates(keep='first', inplace=True)
df.reset_index(drop=True)
# 保存清洗后的DataFrame为新的CSV文件
df.to_csv('../Rinse/clearout_2022.csv', index=False)