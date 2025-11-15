import random
num=100000
n=0
for i in range(num):
    x=random.random()*2-1
    y=random.random()*2-1
    if x*x+y*y<=1:
        n+=1
pi=4.0*n/num
print('计算的圆周率值为：',pi)