fp = open('test.txt','w')
a = 10
for i in range(a):
    # print 函数完整语法 print(value,...sep=" ",end="\n",file=None)
    print(i,file=fp)
fp.close()