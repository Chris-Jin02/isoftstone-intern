# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/1 17:03
# 文件名：auto_test.py

from selenium import webdriver
driver_path = r'D:\anaconda\Scripts\chromedriver.exe'
chrome=webdriver.Chrome()
chrome.get('http://www.baidu.com')

input("按下回车后，浏览器关闭")