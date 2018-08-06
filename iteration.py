# --*--coding:utf-8--*--
# 迭代  for...in...
from collections import Iterable

# list 列表
list1 = list(range(10))
for a in list1:
    print(a)

# dict 字典
dict1 = {'name': 'cf', 'age': 20}
for key in dict1:
    print(key + ":" + str(dict1.get(key)) )

# for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，通过collections模块的Iterable类型判断
print( isinstance(list1, Iterable) )
print( isinstance("asda", Iterable) )
print( isinstance(dict1,Iterable) )

# 循环列表时获取下标
# Python内置的enumerate函数可以把一个list变成索引-元素对
for index,item in enumerate(list1):
    print(str(index) + "--" + str(item))
