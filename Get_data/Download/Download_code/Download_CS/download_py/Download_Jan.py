# 小组：01
# 作者：金石
# 创建时间：2023/6/20 21:37
# 文件名：Download_Jan.py
import requests as req
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import time
headers = {
  'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
}

# HTML string
import requests as req
from bs4 import BeautifulSoup
import lxml
headers = {
 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
htmls = ['https://arxiv.org/list/cs/2301?skip=0&show=1000','https://arxiv.org/list/cs/2301?skip=1000&show=1000','https://arxiv.org/list/cs/2301?skip=2000&show=1000','https://arxiv.org/list/cs/2301?skip=3000&show=1000','https://arxiv.org/list/cs/2301?skip=4000&show=1000','https://arxiv.org/list/cs/2301?skip=5000&show=1000']

def downloaddata(html):
    resp = req.get(html, headers=headers)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, features='lxml')
    papers = soup.find_all(class_='meta')
    print(len(papers))
    data = []
    # 遍历每篇论文的元素，并提取需要的字段的值
    for paper in papers:
        title_element = paper.find(class_='list-title mathjax')
        title = title_element.text.strip().replace('Title:', '')
        if not title:
            title = '未找到数据'

        authors_element = paper.find(class_='list-authors')
        authors = ', '.join([author.text.strip() for author in authors_element.find_all('a')])
        if not authors:
            authors = '未找到数据'

        div = paper.find('div', class_='list-subjects')
        # get the text of the div
        div_text = div.text
        # the subjects are after the string "Subjects:"
        subjects = div_text.split('Subjects:')[1]
        # split the subjects string by "; " to get a list of subjects
        subject = subjects.replace(';', ',').replace('[', '').replace(']', '')
        if not subject:
            subject = '未找到数据'

        text_without_header = soup.h2.text
        date = text_without_header.replace("Authors and titles for", "").strip()
        date = date.replace(", skipping first 1000", "").strip()
        date = date.replace(", skipping first 2000", "").strip()
        date = date.replace(", skipping first 3000", "").strip()
        date = date.replace(", skipping first 4000", "").strip()
        date = date.replace(", skipping first 5000", "").strip()
        date = date.replace(", skipping first 6000", "").strip()
        date = date.replace(", skipping first 7000", "").strip()
        date = date.replace(", skipping first 8000", "").strip()
        date = date.replace(", skipping first 9000", "").strip()
        date = date.replace(", skipping first 10000", "").strip()
        if not date:
            date = '未找到数据'

        categorys = soup.find('div', id='dlpage')
        Category = categorys.h1.text
        if not Category:
            Category = '未找到数据'

        # 将每条论文的字段值组成一个元组，并添加到数据列表中
        data.append((Category, title, authors, subject, date))

    # Define csv file to save the data
    filename = "../Download_csv/Download_Jan 2023.csv"

    # Write data to csv file
    with open(filename, 'a+', newline='', encoding='utf-8') as f:
        # Write the header
        f.write('Category, Title, Authors, Subjects, Date\n')
        # Write the data
        writer = csv.writer(f)
        writer.writerows(data)


    print(f"Data saved to {filename}")
for html in htmls:
    time.sleep(1)
    downloaddata(html)
