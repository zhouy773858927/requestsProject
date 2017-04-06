import datetime

if __name__ == '__main__':
    #输出今日日期，格式为 dd/mm/yyyy
    print(datetime.date.today().strftime('%d/%m/%Y'))

    #创建日期对象宫崎骏出生日期
    miyazakiBirthDay = datetime.date(1941,1,5)
    print(miyazakiBirthDay.strftime('%d/%m/%Y'))

    #日期算数运算timedelta实现日期时间相加
    miyazakiBirthNextDay = miyazakiBirthDay + datetime.timedelta(days = 1)
    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

    #日期替换
    miyazakiBirthFirstDay = miyazakiBirthDay.replace(year=miyazakiBirthDay.year + 1)
    print(miyazakiBirthFirstDay.strftime('%d/%m/%Y'))