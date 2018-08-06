# list - 有序可修改列表

# 初始化时可放入不同类型的参数
list1 = ['a','B',123,True,None]
print(list1)

# 简单的修改
list2 = [1,2,5,6,8,3]
# 在末尾追加
list2.append(8)
print(list2)
#插入制定位置,新增加一个
list2.insert(3,7)
print(list2)
#替换制定位置
list2[4] = 4
print(list2)
# 删除末尾，可输入坐标
list2.pop()
print(list2)
# 排序后的结果作用到自己
list2.sort()
print(list2)
# 获取固定位置
print(list2[2])
print(list2[-1])
# 获取长度
print(len(list2))

#---------------------------
print("------------------")
# tuple 有序集合不可修改列表
tuple1 = (1,10,9,3)
# 排序(因为tuple不允许修改，所以排序时只能返回一个新的元组)
print(sorted(tuple1))
print(tuple1)
# 长度
print(len(tuple1))

# 注意一：
# 初始化一个只有一个元素(无论这个元素是什么类型)的tuple不能只用()包裹，因为python会认为它是括号运算,例如
tuple2 = (True)
print(tuple2)
# 修改为：
tuple2 = (1,)
print(tuple2)

#注意二：
#虽然tuple的内容是不允许修改的，但是这个限制是说tuple的每个元素，指向永远不变。
tuple3 = (1,"sdf",[2,3,4])
tuple3[2][0] = 1
print(tuple3)