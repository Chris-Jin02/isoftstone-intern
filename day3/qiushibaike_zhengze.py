# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/1 15:09
# 文件名：qiushibaike_zhengze.py

import os
import requests as req
import re
from urllib import request

if not os.path.exists('./图片 2'):
    os.mkdir('./图片 2')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
url = 'https://dou.yuanmazg.com/'
resp = req.get(url=url, headers=headers)
resp.encoding = 'utf-8'
# 定义图片的正则
ex = '<div class="col-xs-6 col-sm-3">.*?</div>'
# 判断 page_text 是否符合 ex 定义的正则，re.s:不会对\n 进行中断
imgs = re.findall(ex, resp.text, re.S)
# 输出 0 说明正则定义的有问题--没有匹配到（正则定义的有问题）
print(len(imgs))
# print(type(imgs))
for img in imgs:
    print(type(img))

relative_url = img.split("<")[2]
# 获取 data-original # data- original="/uploads/image/20220124/202201241.jpg"
relative_url = relative_url.split(" ")[4]
# 获取 data-original 里面的值# "/uploads/image/20220124/202201241.jpg"
relative_url = relative_url.split("=")[1]
# 去掉双引号 #/uploads/image/20220124/202201241.jpg
# 从第二位截取到倒数第二位
relative_url = relative_url[1:-1]
print(relative_url)
# relative_url=img('data-original')#真实地址（相对地址）
real_url = 'https://dou.yuanmazg.com' + relative_url
# 根据"/"将对象分割，结果为一个列表（数组），[-1]获取最后一个对象
img_name = relative_url.split('/')[-1]
location_img_path = './图片 2/' + img_name
resp_img = req.get(real_url, headers=headers)

# 从网络上的地址下载到本地的某个地址
request.urlretrieve(real_url, location_img_path)
print(img_name + " 下载成功")
print("完成")
