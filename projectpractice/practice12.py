#判断101-200之间有多少个素数，并输出所有素数。

from math import sqrt
from sys import stdout

h = 0
leap = 1
for k in range(101,201):
    m = int(sqrt(k+1))
    for i in range(2,m + 1):
        if k % i == 0:
            leap = 0
            break
    if leap == 1:
        print('%4d '%k)
        h += 1
        if h % 10 ==0:
            print('')
    leap = 1

print('个数为：%d'%h)