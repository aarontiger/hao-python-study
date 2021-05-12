'''
Author:     DuMin SONG
organization: 光环国际
Project:    linear_regression
software:   PyCharm
'''

a = 4
b = 4
c = a +b
d = a-b
e = 0
try:
    # e = c/d
    with open(file='file2.txt', mode='r', encoding='utf-8') as f:
        data = f.read()
        print(data)
except ZeroDivisionError as z:
    print('z')
    print(z)
except FileNotFoundError as F:
    print('F')
    print(F)
except Exception as E:
    print('E')
    print(E)
finally:
    print('无论是否有异常，都会执行本段代码')
f = c ** d
print(c)
print(d)
print(e)
print(f)