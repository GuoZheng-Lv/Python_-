# 使用input函数后 控制台会进行 打印
username = input('请输入您的姓名:')
print('我的姓名是:'+username)

# 输入整数 也就是 数字 类型
num = input('请输入您的年龄:')
print('您输入的年龄是:' + num) # 在这里还是整数类型
num = int(num)
# print 函数只能链接str(字符串) 类型, 可以使用 , 号进行间隔打印
# print('您输入的年龄是:'+ num) #TypeError: can only concatenate str (not "int") to str
print('您输入的年龄是:' , num)
