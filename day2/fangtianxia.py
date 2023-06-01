# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/5/31 16:43
# 文件名：fangtianxia.py

# 房天下
import requests as req, time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141\
            Safari/537.36'
}

def getAllUrl_details_page(url):

    url_first = url
    resp = req.get(url_first, headers=headers)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, "lxml")

    # href="https://xian.newhouse.fang.com/loupan/3610197054.htm
    # #sjina_C21_02 > a
    a_links = soup.select("div[class='nlcd_name']>a")

    return a_links

def getHourseTDeatil(link):
    # 爬取详情页
    resp = req.get(link, headers=headers)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, "lxml")
    xq_name = soup.find("strong").text
    # print(xq_name)
    price = soup.select(".prib.cn_ff")
    price_single = price[0].text
    price_total = price[1].get_text()
    print(xq_name+'  ---   ---'+price_single + '     ----    ' + price_total)


if __name__ == '__main__':
    for i in range(1, 57):
        url = 'https://xian.newhouse.fang.com/house/s/b9'+str(i)
        a_links = getAllUrl_details_page()
        for link in a_links:
            getHourseTDeatil(link['href'])
