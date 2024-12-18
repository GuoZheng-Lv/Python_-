# eval函数
"""
Python中的内置函数
用于去掉字符串最外侧的引号，并按照Python语句方式执行去掉引号后的字符串
eval()函数经常和inputO函数一起使用

语法 变量=eval(字符串)
"""

s='3.14+3'
print(s,type(s))
x=eval(s) # 使用eval 函数进行去掉s 这个字符串的左右引号, 执行加法运算 也就是 去除引号
print(x,type(x)) # <class 'float'>

# eval() 经常与 input() 一起使用 用于获取用户输入的数值
age=eval(input('亲输入您的年龄:')) # 将字符串类型转换为int类型 相当于 init(age)
print(age,type(age)) # <class 'int'>

height=eval(input('请输入身高:'))
print(height,type(height))  # <class 'float'>



# 如果本身是字符串
hello='北京欢迎你'
print(height)
print(eval('hello')) # 输出了 北京欢迎你 因为去除引号 跟变量名一致 就调用了变量
# print(eval('这种方式是不可以的')) # NameError: name '这种方式是不可以的' is not defined
