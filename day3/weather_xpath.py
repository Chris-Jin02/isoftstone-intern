# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/1 9:31
# 文件名：weather_xpath.py

import requests as req
from lxml import etree as et
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \ AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
resp = req.get('http://www.weather.com.cn/weather/101110101.shtml', headers)
# print(resp.encoding)

resp.encoding = 'utf-8'
# 把请求地址响应结果的文本内容解析称html
page = et.HTML(resp.text)

# 日期
position_date = '//*[@id="7d"]/ul/li[1]/h1/text()'
date = page.xpath(position_date)
print(date[0])

# 天气
position_weather = '//*[@id="7d"]/ul/li[4]/p[1]/text()'
weather = page.xpath(position_weather)
print(weather[0])

# 温度
position_tem1 = '//*[@id="7d"]/ul/li[4]/p[2]/span/text()'
tem1 = page.xpath(position_tem1)
print(tem1[0])
position_tem2 = '//*[@id="7d"]/ul/li[4]/p[2]/i/text()'
tem2 = page.xpath(position_tem2)
print(tem2[0])

# 风向
# @title 获取标签属性的值
position_wind_dir = '//*[@id="7d"]/ul/li[4]/p[3]/em/span[1]/@title'
wind_dir = page.xpath(position_wind_dir)
print(wind_dir[0])

# 风力
position_wind_power = '//*[@id="7d"]/ul/li[4]/p[3]/i/text()'
wind_power = page.xpath(position_wind_power)
print(wind_power[0])

# 7天

