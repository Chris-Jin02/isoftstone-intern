import requests as req
params={'wd':'python'}
#需要折行显示时在末尾添加\
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141\
 Safari/537.36'}
resp=req.get('http://www.baidu.com', params=params,headers=headers)
print(str(resp.content)+'\n')
print(resp.content.decode('utf-8')+'\n')
print(resp.encoding+'\n')
print(resp.url+'\n')
print(resp.status_code)