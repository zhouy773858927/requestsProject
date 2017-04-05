def flatten(nested):#递归生成器
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

def flatten1(nested1):
    try:
        #不要迭代类似字符串的对象
        try:nested1 + ''
        except TypeError: pass
        else:raise TypeError
        for sublist1 in nested1:
            for element1 in flatten1(sublist1):
                yield element1
    except TypeError:
        yield nested1



if __name__ == '__main__':
    nested = [[[1],2],3,4,[5,[6,7]],8]
    print(list(flatten(nested)))
    print("-------------------------------------分割线----------------------------------------")
    nested1 = ['foo',['bar',['baz']]]
    print(list(flatten1(nested1)))