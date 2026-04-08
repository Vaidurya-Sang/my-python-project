#for i in range(10):
 #   print("hello")
  #  print(i)

n = int(input())
sum = 0
for i in range(n+1):
    if i > 0:
        s = 1
        for j in range(i+1):
            if j > 0:
                s *= j
        sum = sum+s
print(sum)

