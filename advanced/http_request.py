import requests
r = requests.get('http://www.sina.comc.cn/') # 豆瓣首页
print(r.status_code)
print(r.text)