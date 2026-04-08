import random
a = random.random()
print(a)
b = random.randint(1,10)
print(b)
print(random.choice("hello"))

a = []
for i in range(20):
    n = random.randint(0,10)
    a.append(n)
print(a)