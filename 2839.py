n = int(input())

idx = 0
if n % 5 == 1 :
    if n > 1:
        idx = int(n / 5) + 1
    else:
        idx = -1

elif n % 5 == 2 :
    if n < 10:
        idx = -1
    else:
        idx = 3
        temp = 12
        while temp <= n:
            temp += 5
            idx += 1
elif n % 5 == 3:
    temp = 3
    while temp <= n:
        temp += 5
        idx += 1

elif n % 5 == 4:
    if n < 5:
        idx = -1
    else:
        idx = 2
        temp = 9
        while temp <= n :
            temp += 5
            idx += 1
else:
    idx = int(n / 5)

print(idx)
