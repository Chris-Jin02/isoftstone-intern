# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/2 11:15
# 文件名：selenium_58_page.py

# 使用 selenium 爬取 58 第一页的岗位信息
from selenium import webdriver  # 浏览器驱动
from selenium.webdriver.common.by import By  # 按照什么方式查找元素
import time

chrome = webdriver.Chrome()
chrome.get('https://xa.58.com/')  # 打开 58 同城

chrome.find_element(By.XPATH, r'//*[@id="commonTopbar_login"]/a[1]').click()
time.sleep(1)
# 切换到账号密码登录
chrome.find_element(By.XPATH, r'//*[@id="mask_body"]/div[2]/div[1]/span[1]').click()
time.sleep(1)
# 输入用户名,密码，点击登录按钮
chrome.find_element(By.XPATH, r'//*[@id="mask_body_item_username"]').send_keys('17789799030')
chrome.find_element(By.XPATH, r'//*[@id="mask_body_item_newpassword"]').send_keys('feige123')
chrome.find_element(By.XPATH, r'//*[@id="mask_body_item_login"]').click()
time.sleep(1)
# 向输入框中输入招聘（搜索内容）
chrome.find_element(By.ID, r'keyword').send_keys('招聘')
# 点击搜索按钮
chrome.find_element(By.ID, r'searchbtn').click()
# 以上代码无论爬取一个岗位还是一页岗位或者是所有页的岗位都要进行的操作
current_window_handle = None  # 声明一个句柄


def getFirstPage():
    current_window_handle = chrome.current_window_handle  # 获取当前页面的句柄
    a_links = chrome.find_elements(By.XPATH, r'//*[@id="jingzhun"]/a')
    index = 0
    with open("./58_tong_cheng.csv", "a+", newline="") as f:
        for a_link in a_links:
            a_link.click()  # 点击链接
            info = getPosInfo()
            # a_link=a_link #为了增强程序健壮性
            # toPosInfo(a_link) #为了增强程序健壮性
            index += 1
            f.write(info + "\n")
            print(str(index) + '条写入成功')
            time.sleep(2)
            chrome.switch_to.window(current_window_handle)  # 跳回首页
    chrome.close()  # 关闭首页

# 上面切换页面的代码执行完成，程序才会识别到详细页面
# def toPosInfo(a_link): #为了增强程序健壮性
# a_link.click() #点击链接
# getPosInfo()


def getPosInfo():
    try:
        time.sleep(6)
        for handle in chrome.window_handles:
            if handle != current_window_handle:
                # 进行页面切换--进入到详情页
                chrome.switch_to.window(handle)
        time.sleep(6)
        # 更新时间
        modify_time = chrome.find_element(By.XPATH, r'/html/body/div[3]/div[3]/div[1]/div[1]/span[1]/span').text
        # print(modify_time)

        # 浏览人数
        totalcount_res = ''
        totalcount = chrome.find_element(By.ID, r'totalcount').text
        if totalcount == None or len(totalcount):
            totalcount_res = ''
        else:
            totalcount_res = totalcount
        # print(totalcount)

        # 申请人数
        apply_num = chrome.find_element(By.ID, r'apply_num').text
        # print(apply_num)

        # 职位
        pos_title = chrome.find_element(By.CSS_SELECTOR, r'span[class="pos_title"]').text
        # print(pos_title)

        # 薪水
        pos_salary = chrome.find_element(By.CLASS_NAME, r'pos_salary').text
        # print(pos_salary)

        # 职位第二名称
        pos_name = chrome.find_element(By.CLASS_NAME, r'pos_name').text
        # print(pos_name)

        # 福利
        pos_welfare = chrome.find_element(By.CLASS_NAME, r'pos_welfare').text
        # print(pos_welfare)

        # 岗位条件
        pos_base_condition = chrome.find_element(By.CLASS_NAME, r'pos_base_condition').text
        # print(pos_base_condition)

        # 公司地址
        pos_area = chrome.find_element(By.CLASS_NAME, r'pos-area').text
        # print(pos_area)

        # 公司名称
        company_name_xpath = r'/html/body/div[3]/div[4]/div[1]/div/div[1]/div/div/a'
        company_name = modify_time = chrome.find_element(By.XPATH, company_name_xpath).text
        # print(company_name)

        # 职位描述
        des = chrome.find_element(By.CLASS_NAME, r'des').text
        # print(des)

        info = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (company_name, modify_time, totalcount_res, apply_num, pos_title, pos_salary, pos_name, pos_welfare, pos_base_condition, pos_area, des)
        info = []
        # print(info + "\n")
        return info

    except Exception as e:
        print('错误类型是:', e.__class__.__name__)
        print('错误明细是:', e)
    finally:
        chrome.close()

if __name__ == '__main__':
    getFirstPage()
