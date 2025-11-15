a=int(input("enter the number:"))
if a<=1:
    print("It has no factors other than itself.")
else:
    i=a//2    #使用//整除避免浮点数问题
    while i>0:
        if a%i==0:
            print('The greatest factor of',a,'(other than itself) is:',i)
            break    #打破while 循环
        i-=1
    else:
        print(a,'is prime number')
