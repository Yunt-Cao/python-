s=0
for i in range(1,101):
    if i%2==1:
        continue
    s=s+i
print('1-100的偶数和为：{:.2f}'.format(s))