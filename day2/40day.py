# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/5/31 15:11
# 文件名：40day.py

import requests as req
import json
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141\Safari/537.36','Referer':'http://www.weather.com.cn/weather40d/101110101.shtml'}
resp = req.get('http://d1.weather.com.cn/calendar_new/2023/101110101_202305.html?_=1685520914255', headers=headers)
resp.encoding = 'utf-8'

# 返回的年内容
print(resp.text)

# 内容进行截取，只要等号后面的内容
print(resp.text[11:])
value = json.loads(resp.text[11:]) #将等号后的内容转为 json 对象
print(value[0]['nowday orange']) #只获取第一个对象的日期
print(value[0]['nongli']) #只获取第一个对象的阴历