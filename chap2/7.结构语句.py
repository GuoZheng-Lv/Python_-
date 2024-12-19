# 赋值运算符的顺序 从右到左

# 从上至下 依次执行是 顺序结构
name = '张三'
age = 20
a=b=c=d=100 # 链式赋值
a,b,c,d='room' # 字符串分解赋值
print(name,age,a,b,c,d)
print('-'*40)



# 选择结构
if name == '张三':
    print('测试')
else:
    print('22')


number=eval(input('请输入幸运数字'))
if number > 100:
    print('您输入的大于100')
elif 100 > number > 50:
    print('您输入的再50-100期间')
    if 70> number > 50:
        print('输入的再70-50间')
else:
    print('您输入的小于50')

if number < 100:number=200
print(number)



score = input('请输入成绩等级')
match score:
    case 'A': print('A')
    case 'B': print('B')
    case 'C': print('C')
    case 'D': print('D')
    case  _ : print('其余打印')


## renge() 函数 Python 中内置的函数, 产生了一个[n,m] 的整数序列, 但是包含n 不包含M
for i in range(1,10):
    print(i)
    if i % 2 == 0:print(i,'是偶数')

## 实现 1-10的累加和
count=0
for i in range(1,10):
    count+=i
print(count)

## 水仙花数量 100 - 1000
"""
设 输入的是 153 那么 求 100 - 1000 的水仙花数
153 = 3*3*3+5*5*5+1*1*1

个十百位数字 然后三次幂
"""

for i in range(100,1000):
    sd=i%10 # 获取个位    假设 153 % 10 ==> 3
    tens=i//10%10 #获取十位上的数组  153//10 % 10 = 5
    hundred=i//100 #获取百位上的数字  153//100 =>> 1
    if sd**3 + tens**3 + hundred**3 == i:
        print(i)


# 遍历循环的扩展性
## 当for循环正常完成所有迭代时，else子句会被执行；如果循环被break语句中断，则不会执行else子句。

## 在for循环中，else子句在没有被break打断的情况下执行。
## 在while循环中，else子句也在没有被break打断的情况下执行
count = 0
for i in range(1,11):
    count+=i
    if count%10 == 0:
        print(i,' count%10 == 01')
        break
else:
    print(count,'总数')

count = 0
while count < 1000:
    count+=1
    if count==999:
        print(count,'到达了')
else:
    print(count,'结束')



# 1-100之间的累加和
s=0
i=1
while i <= 100:
    s+=i
    i+=1
else:
    print(s,'结束了')


# 用户登录 每次用书输入错误之后 进行提示 三次机会
i = 1
correct = 10
while i <= 3:
    account = input('请输入账号')
    password = input('请输入密码')
    if account == 'admin' and password == '88888888':
        print('系统登录成功')
        i = correct
    else:
        if i != 3:
            print('输入错误请从新输入,您还有', 3 - i,'次机会')
        i+=1
else:
    if i != correct:
        print('您全部输入错误,请查询账户密码')
    else:
        print('登录成功')


