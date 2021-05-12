#数组
array_1 =["one",'tow',"three"]

#tuple
tuple_1= ["apple","banana","orange"]
print(len(array_1))

for number in array_1:
    print(number)

for shuiguo in tuple_1:
    print(shuiguo)

#dict
dic_1 ={"name":'郝树虎','weight':70}
keys = dic_1.keys()
print(keys.__class__)
for key in keys:
    print(key);

#set
s=set("小明","丽丽")
s.add('haoshuhu')
print(len(s))
print(s)

#while
sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print(sum)

#if-else
age = int(input('Input your age: '))

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

