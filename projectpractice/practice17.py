#题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

import string
s = input('请输入一串字符：\n')
letters = 0#字母
space = 0#空格
digit = 0#数字
others = 0#其他字符

for i in s :
    if i.isalpha():
        letters += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        digit += 1
    else:
        others += 1
print('litter = %d ,space = %d,digit = %d,others = %d'%(letters,space,digit,others))