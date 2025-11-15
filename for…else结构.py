for i in range(3):
    user_name = input('请输入您的用户名：')
    password = input('请输入您的密码：')
    # 登陆操作 if……else
    if user_name == '曹云涛' and password == '5408':
        print('正在登陆在，请稍后…………')
        # break退出循环 或者可以使用i=8<3来破坏while重复
        break
    else:
        if i < 2:
            print('密码或用户名不正确,你还有', 2 - i, '次机会')
else:
    print('您的机会用光')