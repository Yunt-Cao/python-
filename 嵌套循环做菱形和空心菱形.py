row=eval(input('请输入菱形的行数:'))
#菱形的上半部分
top_row=(row+1)//2
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ',end='')
    for k in range(1, 2 * i):  # 2*i表示*的数量
        print('*', end='')
    print()
bottom_row=row//2
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):  # 1--range(1,8), 2---range(1,6), 3---range(1,4), range(1,2)
        print('*', end='')
    print()


row=eval(input('请输入菱形的行数:'))
#菱形的上半部分
top_row=(row+1)//2
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ',end='')
    for k in range(1, 2 * i):# 2*i表示*的数量
        if k==1 or k==2*i-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
bottom_row=row//2
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):  # 1--range(1,8), 2---range(1,6), 3---range(1,4), range(1,2)
        if k==1 or k==2*bottom_row-2*i+2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
