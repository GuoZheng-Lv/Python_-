# 三行四列 长方形
for i in range(1,4): # 外层循环
    for j in range(1,5): # 内层循环
        end = ' '
        if j == 4:end = '\n'
        print('*',end=end)
print('-' * 10)
# 正三角形
for i in range(1,6):
    for j in range(1,i + 1):
        print('*', end=' ')
    print()

print('-' * 10)
# 倒三角形
for i in range(1,6):
    for j in range(1 ,7 - i):
        print('*', end=' ')
    print()
print('-' * 10)
# 等腰三角形
for i in range(1,6):
    for j in range(1,6-i):
        print(' ', end=' ')
    for k in range(1,i*2):
        print('*', end=' ')
    print()

