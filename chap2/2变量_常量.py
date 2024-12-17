luck_number=8 # 创建一个变量名叫做 luck_number ,并且赋值为8
my_name='吕国正' # 字符串类型的变量

# type 查看数据的具体数据类型
print('luck_number的数据类型是:',type(luck_number)) # <class 'int'>
print('my_name的数据类型是:',type(my_name)) # <class 'str'>
print(my_name,'的年龄',luck_number)


# Python 可以动态修改变量的数据类型,通过赋不同类型的值可以直接修改
my_name='你猜谁' # 修改my_name的值
print(my_name,'的年龄',luck_number)

# 可以将同一个值付给多个变量 同事多个变量指向的是一个值
no=my_name
print(no,my_name)
# 如果想查看这个值是否是一个内存地址可以使用 id() 这个方法进行查看数据内存地址
print(id(no),id(my_name))

"""
变量命名应遵循以下几条规则
》变量名必须是一个有效的标识符
》变量名不能使用Python中的保留字
》慎用小写字母I（挨）和大写字母O
》应选择有意义的单词作为变量名

常量命名应遵循以下几条规则
》常量就是在程序运行过程中，值不充许改变的量
》全部使用大写字母和下划线命名
"""




pi=3.1415926 # 变量
PI=3.1415926 # 常量