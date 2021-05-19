import  redis
ip = '127.0.0.1'
password = 'Admin100%'

conn_pool = redis.ConnectionPool(host=ip,password=None, port=6379)
r = redis.Redis(connection_pool=conn_pool)
r.set('name','haoshuhu')
# r.set('company','bingoyes')
print(r.get('name'))