# 作者：姜何飞飞
# 创建时间：2023/5/31 9:51
# 中国天气网7-15天数据
# 文件名：01.py

import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# useragent可能会随机失败

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 90.0.4430.72Safari / 537.36'}

resp = req.get('http://www.weather.com.cn/weather15d/101110101.shtml', headers=headers)

resp.encoding = 'utf-8'
soup = BeautifulSoup(resp.text)
element_date = soup.find_all("span", class_="time")
# print(type(element_date))

wea = soup.select('.wea')

tem = soup.select('.tem')
for tag in tem:
    print(tag.get_text())

win_direction = soup.select(".wind")

win_power = soup.select(".wind1")

with open("./weather_soup.csv", "a+") as f:
    for i in range(len(wea)):
        print(element_date[i].get_text()+","+wea[i].get_text()+","+tem[i].get_text()+","+win_direction[i].get_text()+","+win_power[i].get_text())
        f.write(element_date[i].get_text()+","+wea[i].get_text()+","+tem[i].get_text()+","+win_direction[i].get_text()+","+win_power[i].get_text()+"\n")
