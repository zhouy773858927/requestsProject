#斐波那契数列。

def fibs(n):
    a,b = 1,1
    for i in range(n - 1):
        a,b = b,a + b
    return a
print(fibs(10))
