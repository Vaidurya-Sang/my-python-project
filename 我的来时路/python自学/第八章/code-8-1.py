def sum_2(a,b):
    return a+b
result = sum_2(1,2)
print(result)

def infos(name,age,gender):
    return "我是%s，我今年%d岁，我性别%s"%(name,age,gender)
a = infos("szw",22,"男")
print(a)

# 可变参数
def total(*c):
    sum1 = 0
    for i in c:
        sum1 += i**2
    return sum1
print(total(1,2,3))


