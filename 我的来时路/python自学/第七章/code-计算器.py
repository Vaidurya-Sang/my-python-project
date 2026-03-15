
while True:
    try :
        op = input("请输入算式")
        if "+" in op:
            a = op.split("+")
            result = int(a[0]) + int(a[1])
            print(result)
        elif "-" in op:
            a = op.split("-")
            result = int(a[0]) - int(a[1])
            print(result)
        elif "*" in op:
            a = op.split("*")
            result = int(a[0]) * int(a[1])
            print(result)
        elif "/" in op:
            a = op.split("/")
            result = int(a[0]) / int(a[1])
            print(result)
        elif op == "C" :
            print("结束")
            break
        else :
            raise Exception("请按1+2格式输入")
    except ZeroDivisionError:
        print("注意除数不能为0")
    except Exception as e:
        print(e)
