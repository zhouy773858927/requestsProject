#暂停十秒输出，并格式化当前时间。

import time
#time.strftime()可以用来获得当前时间，可以将时间格式化为字符串等等
#time.localtime()可以用来获得当前时间
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

time.sleep(10)

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))