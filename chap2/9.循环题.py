answer='y'
while answer=='y':
    print('----------欢迎使用拆线呢-------------')
    print('1.余额')
    print('2.流量')
    print('3.童话')
    print('0.退出')
    choice=int(input('请输入查询项目'))
    match choice:
        case 1:
            print('余额3.00元')
        case 2:
            print('流量22..3123')
        case 3:
            print('通话12314')
        case 0:
            answer='n'
        case _:
            print('请从新输入')
else:
    print('退出成功')


if answer == 'n':
    print('结束')



