# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/9 9:12
# 文件名：arxiv.py


import requests as req
from lxml import etree as et
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \ AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
resp = req.get('https://arxiv.org/list/cs.AI/recent', headers)
# print(resp)
# print(resp.encoding)
# print(resp.text)
# resp.encoding = 'utf-8'
# 把请求地址响应结果的文本内容解析称html
page = et.HTML(resp.text.encode('utf-8'))
# html = et.HTML(resp.text)
# print(page)
# 论文名称
paper_name = '//*[@id="dlpage"]/dl/dd[1]/div/div[1]/text()'
name = page.xpath(paper_name)
print(name[1])
