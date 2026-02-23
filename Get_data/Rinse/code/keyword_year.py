# 作者：金石
# 创建时间：2023/6/28 23:30
# 文件名：keyword_year.py
import csv
from collections import Counter
#数据提取

def count_word_frequency(csv_file, output_csv):
    # 打开CSV文件
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # 使用分号作为分隔符（示例）
        # 提取"subject"列的数据并统计词频
        subject_column = [row[' Subjects'] for row in reader]
        keywords = [subject.split(',') for subject in subject_column]
        keyword_frequency = Counter(keyword for sublist in keywords for keyword in sublist)
        sorted_keywords = keyword_frequency.most_common()
        # 写入CSV文件
        with open(output_csv, mode='w', newline='', encoding='utf-8') as output_file:
            writer = csv.writer(output_file)

            # 写入标题行
            writer.writerow([' Subjects', 'frequency'])

            # 写入词频统计数据
            for word, frequency in sorted_keywords:
                writer.writerow([word, frequency])


# 使用示例
csv_file_path = '/Users/steve/Desktop/项目/大屏/Rinse/clearout_2022.csv'
output_csv_file_path = '../keywords_2022.csv'
count_word_frequency(csv_file_path, output_csv_file_path)


