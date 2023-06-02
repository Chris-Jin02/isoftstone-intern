# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/2 9:29
# 文件名：selenium_58.py

from selenium import webdriver #浏览器驱动
from selenium.webdriver.common.by import By
# 按照什么方式查找元素
import time
chrome = webdriver.Chrome()

# 打开 58 同城
chrome.get('https://xa.58.com/')

# 点击登录按钮
# chrome.find_element_by_xpath('//*[@id="commonTopbar_login"]/a[1]').click()
chrome.find_element(By.XPATH, r'//*[@id="commonTopbar_login"]/a[1]').click()
time.sleep(1)

# 切换到账号密码登录
chrome.find_element(By.XPATH, r'//*[@id="mask_body"]/div[2]/div[1]/span[1]').click()
time.sleep(1)

# 输入用户名密码并登录
chrome.find_element(By.XPATH, r'//*[@id="mask_body_item_username"]').send_keys('17789799030')
chrome.find_element(By.XPATH, r'//*[@id="mask_body_item_newpassword"]').send_keys('feige123')
chrome.find_element(By.XPATH, r'//*[@id="mask_body_item_login"]').click()
time.sleep(1)
# 点击招聘
chrome.find_element(By.ID, r'keyword').send_keys('招聘')
time.sleep(3)

# 点击搜索
chrome.find_element(By.ID, r'searchbtn').click()
time.sleep(3)

# 点击每一个岗位
chrome.find_element(By.XPATH, r'//*[@id="jingzhun"]/a').click()
time.sleep(6)

# 切换浏览器
current_window_handle = chrome.current_window_handle #获取当前页面的句柄
for handle in chrome.window_handles:
    if handle != current_window_handle:
        chrome.switch_to.window(handle) #进行页面切换--下一个页面
time.sleep(6)

# 上面切换页面的代码执行完成，程序才会识别到详细页面
# 更新时间
modify_time = chrome.find_element(By.XPATH, r'/html/body/div[3]/div[3]/div[1]/div[1]/span[1]/span').text
print(modify_time)

# 浏览人数
totalcount = chrome.find_element(By.ID, r'totalcount').text
print(totalcount)

# 申请人数
apply_num = chrome.find_element(By.ID, r'apply_num').text
print(apply_num)

# 职位
pos_title = chrome.find_element(By.CSS_SELECTOR, r'span[class="pos_title"]').text
print(pos_title)

# 薪水
pos_salary = chrome.find_element(By.CLASS_NAME, r'pos_salary').text
print(pos_salary)

# 职位第二名称
pos_name=chrome.find_element(By.CLASS_NAME, r'pos_name').text
print(pos_name)

# 福利
pos_welfare=chrome.find_element(By.CLASS_NAME, r'pos_welfare').text
print(pos_welfare)

# 岗位条件
pos_base_condition=chrome.find_element(By.CLASS_NAME, r'pos_base_condition').text
print(pos_base_condition)

# 公司地址
pos_area=chrome.find_element(By.CLASS_NAME, r'pos-area').text
print(pos_area)

# 公司名称
company_name_xpath = r'/html/body/div[3]/div[4]/div[1]/div/div[1]/div/div/a'
company_name = modify_time = chrome.find_element(By.XPATH, company_name_xpath).text
print(company_name)

# 职位描述
des = chrome.find_element(By.CLASS_NAME, r'des').text
print(des)
input("按下回车后，浏览器关闭")
