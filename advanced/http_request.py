import requests
r = requests.get('http://www.sina.comc.cn/') # 新浪首页
print(r.status_code)
print(r.text)