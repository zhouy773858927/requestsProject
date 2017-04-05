class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self

class TestIterator:
    vaule = 0
    def __next__(self):
        self.vaule += 1
        if self.vaule > 10: raise StopIteration
        return self.vaule
    def __iter__(self):
        return self

if __name__ == '__main__':
    fibs = Fibs()
    for f in fibs:
        if f > 1000:
            print(f)
            break
    ti = TestIterator()

print("-------------------------------------------第一次分割线------------------------------------------")
it = iter([1,2,3,4,5])
print(it.__next__())
print(it.__next__())
print("-------------------------------------------第二次分割线------------------------------------------")
print(list(ti))

