year = int(input("输入年份"))
if year % 100 ==0:
    if year % 400==0:
        print("是闰年")
    else:
        print("不是闰年")
elif year % 4==0:
    print("是闰年")
else:
    print("不是闰年")








