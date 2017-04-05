def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element#yield生成器
if __name__ == '__main__':
    nested = [[1,2],[3,4],[5]]
    for num1 in nested:
        print(num1)
    print("--------------------------------------第一次分割线-----------------------------------------")
    for num in flatten(nested):
        print(num)
    print("--------------------------------------第二次分割线-----------------------------------------")
    print(list(flatten(nested)))