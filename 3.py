class Rectangle:
    def __init__(self):
        self.width = 0
        self.hight = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.hight,self.width = value
        else:
            self.__dict__[name] = value#为了避免_setattr_被再次调用
    def __getattr__(self, name):
        if name == 'size':
            return self.hight,self.width
        else:
            AttributeError

if __name__ == '__main__':
    rt = Rectangle()
    rt.hight = 10
    rt.width = 5
    #print(rt.__setattr__('size', (11, 6)))
    print(rt.__getattr__('size'))


