#长方形
for i in range(1,4):
    for j in range(1,5):
        print('*',end='')
    print()
print('-'*1000)
#直角三角形
for i in range(1,5):
    for j in range(1,i+1):
        print('*',end='')
    print()
print('-'*1000)
#倒三角形
for i in range(1,5):
    for j in range(1,6-i):
        print('*',end='')
    print()
print('-'*1000)
#等腰三角形
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1,2*i):  #2*i表示*的数量
        print('*',end='')
    print()
print('-'*1000)