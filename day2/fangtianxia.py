# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/5/31 16:43
# 文件名：fangtianxia.py

# 房天下
import requests as req, time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 90.0.4430.72Safari / 537.36'}

url_first = "https://xian.newhouse.fang.com/house/s/b91/"

resp = req.get(url_first, headers=headers)
a_link = soup.select("div[class='nlcd_name']>a")
resp.encoding = 'utf-8'
soup = BeautifulSoup(resp.text, "lxml")
xiaoqu_name = soup.find("strong").text

link_detail = a_link[0]['href']


print(xiaoqu_name)