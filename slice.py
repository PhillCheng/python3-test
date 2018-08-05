# slice -截取，可截取list、tuple、str,包含3个参数(start, stop[, step])

list1 = list(range(10))
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
print( list1[0:3] )
# 如果起始位为0，也可以省略
print( list1[:3])
'''
前10个数，每两个取一个,最后一个参数为间距
'''
print(list1[:10:2])
# [:]为复制一个新的列表
print(list1[:])

# 字符串的截取，返回结果依然是字符串
str1 = "Hello there!"
print(str1[0:5])

# slice 对象处理
mySlice = slice(0,5,2)
print(str1[mySlice])

