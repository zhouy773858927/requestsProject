#暂停一秒输出
#dict.items()此方法返回元组对的列表。

import time
myd = {1:'a',2:'b'}
for key,value in dict.items(myd):
    print(key,value)
    time.sleep(1)#暂停1秒