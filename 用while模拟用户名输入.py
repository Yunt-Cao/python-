# (1)初始化变量
i=0
while i<3: #(2)条件判断0，1，2
    #(3)语句块
    user_name=input('请输入您的用户名：')
    password=input('请输入您的密码：')
    #登陆操作 if……else
    if user_name=='曹云涛' and password=='5408':
        print('正在登陆在，请稍后…………')
        #break退出循环 或者可以使用i=8<3来破坏while重复
        break
    else:
        if i<2:
            print('密码或用户名不正确,你还有',2-i,'次机会')
    i+=1  #相等于i=i+1  (4)改变变量
#单分支的判断 当三次都不对,循环结束,i的最大值为3
if i==3:
    print('对不起，您已输入错误三次')


