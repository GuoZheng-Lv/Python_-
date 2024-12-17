a = 100 # 定义变量a 赋值100
b = 200
print(90)
print(a)
print(a * b) # 输出乘法运算结果

## 可以使用多个引号进行打印
print('单引号打印')
print("双引号打印")
print('''三个单引号打印''')
print("""多个双引号打印""")

## 不换行输入输出
print(a,b,'不换行输出')

## 输出ASCII码及打印所对应的数据
print('b')
print(chr(98))
print('C')
print(chr(67))
print(8)
print(chr(56))
print('[')
print(chr(91))
### 中文编码的范围是[u4e00~u9fa5]

print(ord('北')) # 使用ord 函数进行打印相应编码  21271
print(chr(21271)) # chr 函数进行打印相应文字 北



## 如何不换行进行打印
# value, 是你输入的值,你输入的必须要在最前面, sep 是打印出来间隔符号,end是 打印结尾的符号, \n 换行符 file是 文件
# print 函数完整语法 print(value,...sep=" ",end="\n",file=None)

print('北京', end='===>')
print('欢迎你','测试sep',sep='、')

## 使用连接符进行链接
print('链接' + '链接成功')
# 只能链接字符串
# print('链接' + 200) # TypeError: can only concatenate str (not "int") to str
