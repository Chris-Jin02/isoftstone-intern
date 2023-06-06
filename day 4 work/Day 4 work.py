# 小组：01
# 作者：金石
# 创建时间：2023/6/6 16:17
# 文件名：Day 4 work.py
from selenium import webdriver   #浏览器驱动
from selenium.webdriver.common.by import By #按照什么方式查找元素
import  time
chrome=webdriver.Chrome()
chrome.get('https://xa.58.com/')#打开58同城
#点击登录按钮
chrome.find_element(By.XPATH,'//*[@id="commonTopbar_login"]/a[1]').click()
time.sleep(1)
#切换到账号密码登录
chrome.find_element(By.XPATH,'//*[@id="mask_body"]/div[2]/div[1]/span[1]').click()
time.sleep(1)
#输入用户名,密码，点击登录按钮
chrome.find_element(By.XPATH,'//*[@id="mask_body_item_username"]').send_keys('13589351009')
chrome.find_element(By.XPATH,'//*[@id="mask_body_item_newpassword"]').send_keys('jinshi1234')
chrome.find_element(By.XPATH,'//*[@id="mask_body_item_login"]').click()
time.sleep(1)
#向输入框中输入招聘（搜索内容）
chrome.find_element(By.ID, r'keyword').send_keys('招聘')
time.sleep(1)
# 点击搜索
chrome.find_element(By.ID, r'searchbtn').click()
time.sleep(1)
#以上代码无论爬取一个岗位还是一页岗位或者是所有页的岗位都要进行的操作
current_window_handle=None #声明一个句柄
def getFirstPage():
    # 切换浏览器
    current_window_handle = chrome.current_window_handle #获取当前页面的句柄
    a_links= chrome.find_elements(By.XPATH,'//*[@id="list_con"]/li[*]/div[1]/div/a') #获取的就是一组对象(获取所有的链接) 28
    print(len(a_links))
    index=0
    with open("./58_allPage.csv", "a+", newline=None,encoding='utf-8') as f:
        for a_link in a_links:
            a_link.click() #点击链接
            info=getPosInfo()
            # a_link=a_link #为了增强程序健壮性
            # toPosInfo(a_link) #为了增强程序健壮性
            index += 1
            f.write(info + "\n")
            print(str(index) + '条写入成功')
            time.sleep(1)
            chrome.switch_to.window(current_window_handle)  # 跳回首页

def getAllpage():
    for i in range(9):
        getFirstPage()
        chrome.find_element(By.CLASS_NAME,'next').click()


def getPosInfo():
    try:
        time.sleep(1)
        for handle in chrome.window_handles:
            if handle != current_window_handle:
                chrome.switch_to.window(handle)  # 进行页面切换--进入到详情页
        time.sleep(0.3)

        # 更新时间
        modify_time_list = [element.text for element in chrome.find_elements(By.XPATH,'/html/body/div[3]/div[3]/div[1]/div[1]/span[1]/span')]
        modify_time = '\n'.join(modify_time_list)
        if not modify_time:
            modify_time = '未找到数据'
        # print(modify_time)
        time.sleep(0.3)
        print('更新时间:\n'+modify_time)

        # 浏览人数
        totalcount_list = [element.text for element in chrome.find_elements(By.ID,'totalcount')]
        totalcount = '\n'.join(totalcount_list)
        if not totalcount:
            totalcount = '未找到数据'
        # print(totalcount)
        time.sleep(0.3)
        print('浏览人数:\n'+totalcount)

        # 申请人数
        apply_num_list = [element.text for element in chrome.find_elements(By.ID,'apply_num')]
        apply_num = '\n'.join(apply_num_list)
        if not apply_num:
            apply_num = '未找到数据'
        # print(apply_num)
        time.sleep(0.3)
        print('申请人数:\n'+apply_num)

        # 职位
        pos_title_list = [element.text for element in chrome.find_elements(By.CSS_SELECTOR, 'span[class="pos_title"]')]
        pos_title = '\n'.join(pos_title_list)
        pos_title = pos_title.replace('\n','')
        pos_title = pos_title.replace(',','，')
        # print(pos_title)
        if not pos_title:
            pos_title = '未找到数据'
            time.sleep(0.3)
        print('职位:\n'+pos_title)

        # 薪水
        pos_salary_list = [element.text for element in chrome.find_elements(By.CLASS_NAME,'pos_salary')]
        pos_salary = '\n'.join(pos_salary_list)
        pos_salary = pos_salary.replace('\n','')
        pos_salary = pos_salary.replace(',','，')
        # print(pos_salary)
        if not pos_salary:
            pos_salary = '未找到数据'
        time.sleep(0.3)
        print('薪水:\n'+pos_salary)

        # 职位第二名称
        pos_name_list = [element.text for element in chrome.find_elements(By.CLASS_NAME,'pos_name')]
        pos_name = '\n'.join(pos_name_list)
        pos_name = pos_name.replace('\n','')
        pos_name = pos_name.replace(',','，')
        # print(pos_name)
        if not pos_name:
            pos_name = '未找到数据'
        time.sleep(0.3)
        print('职位第二名称:\n'+pos_name)

        # 福利
        pos_welfare_list = [element.text for element in chrome.find_elements(By.CLASS_NAME,'pos_welfare')]
        pos_welfare = '\n'.join(pos_welfare_list)
        pos_welfare = pos_welfare.replace('\n','')
        pos_welfare = pos_welfare.replace(',','，')
        # print(pos_welfare)
        if not pos_welfare:
            pos_welfare = '未找到数据'
        time.sleep(0.3)
        print('福利:\n'+pos_welfare)

        # 岗位条件
        pos_base_condition_list = [element.text for element in chrome.find_elements(By.CLASS_NAME,'pos_base_condition')]
        pos_base_condition_join = '\n'.join(pos_base_condition_list)
        pos_base_condition = pos_base_condition_join.replace(',','，')
        pos_base_condition = pos_base_condition.replace('\n','')
        # print(pos_base_condition)
        if not pos_base_condition:
            pos_base_condition = '未找到数据'
        time.sleep(0.3)
        print('岗位条件:\n'+pos_base_condition)

        # 公司地址
        pos_area_list = [element.text for element in chrome.find_elements(By.CLASS_NAME,'pos-area')]
        pos_area='\n'.join(pos_area_list)
        pos_area = pos_area.replace('\n','')
        pos_area = pos_area.replace(',','，')
        # print(pos_area)
        if not pos_area:
            pos_area = '未找到数据'
        time.sleep(0.3)
        print('公司地址:\n'+pos_area)

        #公司名称
        company_name_list = [element.text for element in chrome.find_elements(By.XPATH,'/html/body/div[3]/div[4]/div[1]/div/div[1]/div/div[1]/a' or'/html/body/div[3]/div[4]/div[1]/div/div[1]/div[1]/a')]
        company_name='\n'.join(company_name_list)
        company_name = company_name.replace('\n','')
        company_name = company_name.replace(',','，')
        # print(company_name)
        if not company_name:
            company_name = '未找到数据'
        time.sleep(0.3)
        print('公司名称:\n'+company_name)

        #职位描述
        des_list = [element.text for element in chrome.find_elements(By.CLASS_NAME, 'des')]
        des_join = '\n'.join(des_list)
        des = des_join.replace('\n','')
        des = des.replace(',','，')
        if not des:
            des = '未找到数据'
        time.sleep(1)
        print('职位描述:\n'+des)


        info='%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (company_name,modify_time,totalcount,apply_num,pos_title,pos_salary,pos_name,pos_welfare,pos_base_condition,pos_area,des)
        #print(info+"\n")
        return info
    except Exception as e: #总异常
        print('错误类型是:',e.__class__.__name__)
        print('错误明细是:',e)
        #如果出现异常-将出错的这条信息重新进行爬取，#为了增强程序健壮性
        # getPosInfo(a_link) #出错的情况下才 递归：直接或间接调用方法本身
    finally:
        chrome.close() #关闭详情页



if __name__ == '__main__':

    getAllpage()