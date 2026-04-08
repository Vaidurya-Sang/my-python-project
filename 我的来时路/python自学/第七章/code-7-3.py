try:
    pwd = input("输入密码")
    if len(pwd)<8:
        raise Exception("长度不够")
except Exception as e:
    print(e)

