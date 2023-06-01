# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/1 15:24
# 文件名：ftx_multi_thread.py

import requests as req, time, threading
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141\
            Safari/537.36'
}

def getAllUrl_page():  # h获取每一页的链接，共45页
    start = time.process_time()
    with open('./房天下所有页_多线程2.csv', 'a+') as f:
        f.write('小区名称,评分,特色,价格,主推房型,项目地址,近期开盘\n')
        index = 0
        for i in range(1, 3):  # (1,2]
            #    https://     newhouse.fang.com/house/s/b936/  全国
            url = "https://xian.newhouse.fang.com/house/s/b9" + str(i)
            # print(url)
            a_link = getAllUrl_details_page(url)
            for link in a_link:
                # print('详情链接:  '+link['href']) #通过属性名称获取属性值
                # house_info = getHouseInfo(link['href'])
                # # print(house_info)
                # print("*" * 30)
                # f.write(house_info + "\n")
                # target  ---调用的目标方法名，args----参数
                href =link['href']
                # print(href)
                th = threading.Thread(target=getHouseInfo, args=(href,))  # 一个参数时也要加“,”
                th.start() #启动多线程

                index += 1
                print(str(index) + "条写入成功")
        end = time.process_time()
        print(str(index) + "条写入成功,共花费" + str(end - start))


def getAllUrl_details_page(url_page):  # 获取每一页中每个岗位的详细链接（也可获取更多详细信息按钮的链接）
    resp = req.get(url_page, headers=headers)
    resp.encoding = 'utf-8'
    # print(resp.text)
    soup = BeautifulSoup(resp.text, 'lxml')
    a_doms = soup.select("div[class='nlcd_name']>a")
    # print(len(a_doms))
    return a_doms


def getHouseInfo(url_details):  # 获取岗位信息--参数为详情页链接
    resp = req.get(url_details, headers=headers)
    resp.encoding = 'utf-8'

    soup = BeautifulSoup(resp.text, 'lxml')
    # 每次查找数据时就可以从此div中查找，尽可能的缩小查找范围
    # information=soup.select("div[class='information']")

    # house_name=soup.select("div[class='information'] strong") #空格 找到所有的子元素
    # 找到第一个子元素
    # 小区名称               #sjina_C23_02 > a  document.querySelector("#sjina_C23_02 > a"

    house_name = soup.select("div[class='information']>div>div>h1>strong")[0].text
    # print(house_name)
    # 评分
    house_score = soup.select("div[class='information']>div>div>a")[0].text
    # print(house_score)

    # 小区特色
    house_feature = soup.select("div[class='biaoqian1']")[0].find_all("a")  # 获取此div中的所有的a标签
    # print(house_feature[0].text)

    # print(len(house_feature))

    house_feature2 = ""  # 特色
    for feature in house_feature:
        # temp="-"+temp+feature.text
        t = "-" + feature.text
        house_feature2 = '%s%s' % (house_feature2, t)  # 拼接，在python中这种拼接方式是官方所提倡
    # print(house_feature2)
    # print("*"*50)

    # 价格
    house_price = soup.select(".prib.cn_ff")[0].text
    # for price in house_price:
    #     print(price.text)
    # print(house_price)

    # 价格参考内容
    price_refer = soup.select(".info_price")
    if len(price_refer) > 0:
        price_refer = price_refer[0].text
        # print("="*50)
        # print(price_refer)
        # print("*"*50)

    # 主力户型
    house_type = soup.select(".fl.zlhx>a")
    type2 = ""  # 户型
    for a in house_type:
        # print(a.text)
        t = "-" + a.text
        type2 = '%s%s' % (type2, t)

    # print(type2)
    # 地址
    address = soup.select("div[id='xfptxq_B04_12']>span")[0].text
    # print(address)

    # 近期开盘
    house_open = soup.select("div[class='inf_left fl']>a")[0].text
    # print(house_open)

    # house_info=house_name+","+"house_score"+","+house_feature2+","+house_price+","+price_refer+","+type2+","+address+","+house_open

    house_info = "%s,%s,%s,%s,%s,%s,%s" % (house_name, house_score, house_feature2, house_price, type2,
                                           address, house_open)
    with open("./房天下所有页_多线程2.csv", "a+", newline=None) as f:
        f.write(house_info + "\n")
    return house_info


if __name__ == "__main__":
    getAllUrl_page()