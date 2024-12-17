# 1. 使用print函数 将人生苦短 我用Python 输出到文件text.tex中
fp=open('text.txt','w') # 打开文件
print('人生苦短 我用Python',file=fp) # 将打印输出到文件里面
fp.close() # 关闭文件

# 2.输出个人自我介绍
## 使用input 函数从键盘输入姓名、年龄、座右铭,并使用函数输出到控制台
username = input('请输入您的姓名: ')
age = int(input('请输入您的年龄: '))
motto = input('请输入您的座右铭: ')
print('------自我介绍------')
print('姓名:', username)
print('年龄:', age)
print('座右铭:', motto)
