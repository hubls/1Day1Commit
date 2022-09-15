import math

m, n = input().split()
m = int(m)
n = int(n)


for i in range(m, n+1):
    idx = 0
    if i == 1:
        continue
    for j in range(1, int(math.sqrt(i)) + 1):
        if(i % j == 0):
            idx += 1
            if idx == 2:
                break
    if idx == 1:
        print(i)
