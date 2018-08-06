# dict  dictionary 字典 类似于map
dict1 = {'name':'cf', 'age':20}
print(dict1)
# 取值
print(dict1['name'])
print(dict1.get('age'))
print(dict1.get('sex','女'))
# 修改
dict1['age'] = 30
print(dict1)
# 动态扩展
if(not 'sex' in dict1) :
    dict1['sex'] = '男'
print(dict1)
# 删除key对应的记录
dict1.pop('sex')
print(dict1)


#--------------------
# set 无序和无重复元素的集合
print('---------------------')
# 注意：set声明必须加关键字
set1 = set([3,2,0,6,50])
print(set1)

#增加
set1.add(7)
print(set1)
# 增加重复的值不会有用
set1.add(3)
print(set1)
# 移除第一位
set1.pop()
print(set1)
# 移除特定的key
set1.remove(50)
print(set1)
