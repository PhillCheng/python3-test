
# 位置参数
def getSum(a,b) :
    c = a * b
    print(c)

getSum(1,3)
#----------------------------
# 位置参数 （列表）
def appendList(arg1):
    arg1.append(3)

list2 = [2,4,5]
appendList(list2)
print(list2)
#-----------------------
# 默认参数
def getSum3(a, b=3) :
    print(a + b)

getSum3(6)
#--------------------------
# 可变参数
def getSum1(a,*arg) :
    # arg 为一个tuple
    print(arg)

# 可变参数的调用
getSum1(1,*(2,3,4))
getSum1(1,2,3,4)
#------------------------
# 关键字参数
def getSum2(a, **kw) :
    # kw为一个dict
    print(kw)

# 关键字参数的调用
getSum2(1,**{'name':'zhangsan','age':20})
getSum2(1,name='zhangsan',age=20)
#-----------------------------------
# 命名关键字参数(为关键字参数增加必填约束)
# 此处表示 name和 age为必须传字段，但是由于age给了默认值，所以可以不传
def getSum4(a, *, name, age="10") :
    print(name +" + "+ age)

getSum4(1,name="123",age="20")
#-----------------------------------
# 命名关键字参数与可变参数同时使用
def getSum5(a,*args,name,age):
    print(args)
    print(name + "+" + age)

getSum5(1,*(1,2,3),name="sdf",age="20")

#---------------------------------------
# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

f1(1,4,*(1,3,4),**{"name": "zhangsan","age": 20})