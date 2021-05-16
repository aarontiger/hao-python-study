'''
Author:     Shuhu Hao
organization: bingoyes
Project:    Python Study
software:   PyCharm
'''

# for 循环
# for i in range(10):
#     print(i)
# print('循环结束')

# list1 = [1,2,3,3,4,5,'james','宾高宜',324.2343,True,{123,3543,'4546'},[23,21,56576]]
# print(list1)
# for e in list1:
#     print(e)

#while循环
# a = 10
# while a>0:
#   a -= 1
#   print(a)
#   print('I am learning Python')
# print('循环结束')

#条件分支
# 每月累计迟到次数超过4次，扣1天工资
# 迟到次数2-4之间，每次扣40元
# 小于等于2次，不扣工资
a = 3
if a>4:
    print('扣一天工资')
elif 2<a<=4:
    print('每次扣40元')
elif 1<a<=2:
    print('每次扣20元')
else:
    print('不扣工资')