x=eval(input('请输入菱形的行数：'))
x_upper=(x+1)//2
for i in range(1,x_upper+1):
    for j in range(1,x_upper+1-i):
        print(' ',end='')
    for k in range(1,2*i):
        print('*',end='')
    print()
x_lower=(x-1)//2
for i in range(1,x_lower+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*x_lower-2*i+2):
        print('*',end='')
    print()