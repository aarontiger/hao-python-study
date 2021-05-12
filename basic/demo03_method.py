'''
Author:     DuMin SONG
organization: 光环国际
Project:    linear_regression
software:   PyCharm
'''
# 用def定义，pass占位
# 调用函数在函数后面

# def info(a,b,c):
#     # print('I am info')
#     d = a+ b+c
#     return d
# print(info(1,2,3),1,2,3,4,5,6)
# tuple1 = (1,2,3,3,4,5,'james','光环国际',324.2343,True)

def sum1(*num):
    add = 0
    for e in num:
        add +=  e
    return add
print(sum1(1,2,3,94))