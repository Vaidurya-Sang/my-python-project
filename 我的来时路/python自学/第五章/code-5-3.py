n = 0
while n >= 0:
    x = int(input("请输入一个数："))
    i = 2
    while i < x:
        if x%i == 0:
            break
        else:
            i += 1
    if i == x:
        print("是质数")
    else:
        print("不是质数")
