import requests as req

url_login = 'http://zc.7k7k.com/post_login'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome/90.0.4430.72Safari/537.36','Origin':'http://zc.7k7k.com','Referer':'http://zc.7k7k.com/minilogin?callback=hdcallback_1620634663110'
}
data = {'username': '2713280507', 'password': '123456', 'autologin':'checked'}
resp_login = req.post(url_login, data=data, headers=headers)
cookies = resp_login.cookies.get_dict()  # 将返回'的 cookie 转换为字典格式
print(cookies)
code = resp_login.status_code
if code == 200:
    url_shoucang = 'http://my.7k7k.com/game/my/faved'
    resp_sc = req.get(url_shoucang, headers=headers, cookies=cookies)
    resp_sc.encoding = 'utf-8'

    # wb二进制文件
    with open('7k7k.html', 'wb') as f:
        f.write(bytes(resp_sc.content))