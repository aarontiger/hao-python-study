
import time

#获取时间戳,单位为秒，包含小数
# ticks = time.time()
# print("当前时间戳为:", ticks)

#时间元组
# localtime = time.localtime(time.time())
# print("本地时间为 :", localtime)
# print(type(localtime))


#日期时间格式化
# 格式化成2016-03-20 11:45:39形式
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
# print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
# print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))