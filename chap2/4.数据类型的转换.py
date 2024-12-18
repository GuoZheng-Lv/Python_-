# 1.数据类型的转换
## 类型转换分为 隐式转换 显式类型
"""
int(x)      将x转为整数类型
float(x)    将x转为浮点数类型
str(x)      将x转为字符串
chr(x)      将整数x转换为一个字符unicode码
ord(x)      将一个字符x转换为对应的整数值
hex(x)      将一个整数x转换为一个十六进制的字符串
oct(x)      将一个整数x转换为一个八进制的字符串
bin(x)      将一个整数x转换为一个二进制的字符串
"""

x=10
y=3
z=x/y # 在执行除法运算的时候,将运算的结果赋值给z  3.3333333333333335
print(z,type(z)) # 隐式转换,将运算隐藏的转为了结果类型 <class 'float'>


### float 类型转成int类型, 只保留整数部分
print('float类型转为int类型:',int(3.14)) # 3
print('float类型转为int类型:',int(3.9)) # 3
print('float类型转为int类型:',int(-3.14))  # -3
print('float类型转为int类型:',int(-3.9)) # -3

### int 类型转成 float 类型
print('int类型转为float类型:',float(10)) # 10.0
print(int('100') + int('200')) # 300
### 将字符串转成int胡总和float时报错的情况
# print(int('18a')) # ValueError: invalid literal for int() with base 10: '18a
# print(int('3.14')) # ValueError: invalid literal for int() with base 10: '3.14'
# print(float('45a.987')) # ValueError: could not convert string to float: '45a.987'

### chr() 和 ord() 是一对
print(ord('吕')) # 21525 在unicode表中对应的整数值
print(chr(21525)) # 吕 将unicode 转成对应文字

### 进制转换
print('十进制转成十六禁止',hex(26472))
print('十进制转成八禁止',oct(26472))
print('十进制转成二禁止',bin(26472))
