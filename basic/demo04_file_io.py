'''
Author:     DuMin SONG
organization: 光环国际
Project:    linear_regression
software:   PyCharm
'''
# f = open(file='file1.txt',mode='r',encoding='utf-8')
# data = f.read()
# print(data)
# f.close()

# with open(file='file1.txt',mode='r',encoding='utf-8') as f:
#     data = f.read()
#     print(data)

f = open(file='file2.txt',mode='w',encoding='utf-8')
f.write('光环国际\n')
f.write('人工智能\n')
f.write('机器学习\n')
f.write('回归算法\n')

with open(file='file3.txt',mode='r',encoding='utf-8') as f:
    data = f.read()
    print(data)