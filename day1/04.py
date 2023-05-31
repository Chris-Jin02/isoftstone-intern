import requests as req

url_login = 'http://zc.7k7k.com/post_login'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 90.0.4430.72Safari / 537.36',

'Origin': 'http://zc.7k7k.com',
'Referer':
'http://zc.7k7k.com/minilogin?callback=hdcallback_1620634663110'
}
data = {'username': '2510280947', 'password': 'a123456789', 'autologin':
    'checked'}
req_session = req.session()
resp_login = req_session.post(url_login, data=data, headers=headers)
code = resp_login.status_code
if code == 200:
    url_shoucang = 'http://my.7k7k.com/game/my/faved'
    resp_sc = req_session.get(url_shoucang, headers=headers)
    resp_sc.encoding = 'utf-8'
    with open('./7k7k2.html', 'wb') as f:
        f.write(bytes(resp_sc.content))
        print('完成')