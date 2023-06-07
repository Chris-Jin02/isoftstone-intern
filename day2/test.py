# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/5/31 16:02
# 文件名：58_page.py
import requests as req
#from fake_useragent import UserAgent #随机请求头
from bs4 import BeautifulSoup
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\AppleWebKit/537.36 (KHTML, like Gecko)Chrome/87.0.4280.141\
 Safari/537.36',
 'Referer':'http://www.weather.com.cn/'
 }
resp=req.get('http://www.weather.com.cn/weather/101110101.shtml',headers=headers)
resp.encoding='utf-8'
soup=BeautifulSoup(resp.text)
element_date=soup.find_all(lambda tag: tag.name == 'h1' and '日' in tag.get_text())

wea=soup.select('.wea')

tem=soup.select('.tem')

win_tags=soup.find_all('span', {'title': lambda x: x and '风' in x})
# 将风向标签按两个为一对进行分组合并
win_pairs = ['转'.join((win_tags[i]['title'], win_tags[i+1]['title'])) for i in range(0, len(win_tags), 2)]

win_power=soup.find_all(lambda tag: tag.name == 'i' and '级' in tag.get_text())