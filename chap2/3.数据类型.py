# 数据类型
from multiprocessing.connection import address_type

## 1. 整数的四种标识形式
num=987 # 默认是十进制,表示整数
num2=0b1010101 # 使用二进制标识整数
num3=0o765 # 使用八进制表示整数
num4=0x87ABF # 使用十六进制表示整数
print(num)
print(num2)
print(num3)
print(num4)


## 2.浮点数
height=187.6 # 身高
print(height)
### type()  查看数据类型
print(type(height)) # float
print(type(num))  # int


### 科学计数法
x=1.99E1413
print('科学计数法:',x,'x的数据类型',type(x)) # <class 'float'>

## 小数计算可能会出现意外
print(0.1 + 0.2) # 0.30000000000000004
## 出现意外后可以通过 round() 函数进行保留两位小数

'''
round() 函数 
@deprecated 用于将浮点数近似指定精度的小数或浮点数近似为整数
语法
round(number, ndigits=None)

number 四舍五入的浮点数
ndigits 需要保留的小数位数, 不传返回整数
'''
print(round(0.1+0.2, 1)) # 0.3



# 3.复数类型
'''
Python中的复数与数学中的复数形式完全一致，由实部和虚部组成
在Python中实数部分使用.real表示，虚数部分使用.imag表示
'''
x=123+456j
print('实数部分',x.real) # 123.0
print('虚数部门',x.imag) # 456.0

# 4.字符串类型
# 单行字符串
city='郑州'
address='郑州市航空港区尚美华庭一号楼一单元1203'
print(city)
print(address)

## 多行字符串
info= ''' 地址:郑州市航空港区尚美华庭一号楼一单元1203
    收件人:吕国正
    手机号:18574154039
'''

info1= """地址:郑州市航空港区尚美华庭一号楼一单元1203
    收件人:吕国正
    手机号:18574154039
"""
print(info)
print('---------上下一致-----------')
print(info1)

## 5.转义字符
"""
\n 换行符
\t 制表符 根据前面文字的数量进行添加空格 一个制表位为8个字符 
"""
# 如果一行中需要添加双引号或者多引号
print('老师说:\"1112314123\"')
print('老师说:"1112314123"')

## 6.原字符, 是转义字符串失效的符号r或者R
print(r'北\n京\n环\n境\n你')
print('北\n京\n环\n境\n你')
print(R'北\n京\n环\n境\n你')


# 7.字符串的索引和切片
s='HELLOWORLD'
print(s[0],s[-10]) # H H 序号0 和序号 -10 标识的是同一个字符
print('背景欢迎你'[4]) # 获取字符串索引位 4
print('背景欢迎你1'[-1],s[len(s)-1]) # 获取最后一位文字
print('--------------------')
print('截取',s[2:7]) # 截取从2开始到7结束的数据字符 不包含七   正向递增
print('截取',s[-8:-3]) # 反向递增
print('截取',s[:5]) # 默认N从0开始
print('截取',s[5:]) # 默认N从第五位开始进行截取
splitEnd=7
print(s[2:splitEnd]) # 使用变量也可以


"""
常用字符串操作
> x+y 将字符串拼接起来
> x*n或者n*x 复制n此字符串x
> x in s 如果x是x的字串 结果为True 否则结果就是False
"""
print('你' + '好') # 链接
print('你' * 3) # 对 你进行复制 3次
print(3 * '你') # 对 你进行复制 3次
y='郑州市航空港'
print('航空' in y) # 包含 True
print('洛阳' in y) # 不包含 False



# 8.布尔类型
""" 布尔类型
用来表示“真”值或“假”值的数据类型
在Python中使用标识符True或False表示布尔类型的值
True表示整数1，False表示整数0

》 False 或者是None
数值中的0，包含0，0.0，虚数0
空序列包含空字符串、空元组、空列表、空字典、空集合
自定义对象的实例，该对象的__bool__()方法返回False或__len__()方法返回0
"""
x=True
print(x)
print(type(x)) # <class 'bool'>
print(x + 10) # 11  ---> 1 + 10
print(False + 10) # 10  ---> 0 + 10

print(bool(18)) # 测试一下整数18的布尔值 True
print(bool(0),bool(0.0)) # False

# 总结, 非0的整数的布尔值都是True
print(bool('北京欢迎你')) # True
print(bool("")) # False
# 所有非空字符串的布尔值都是True
print(bool(False)) # False
print(bool(None)) # False