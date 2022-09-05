m = int(input())
n = int(input())


lst = []
for i in range(m, n+1):
    idx = 0
    for j in range(2,i+1):
        if i % j == 0:
            idx +=1
    if idx == 1:
        lst.append(i)


if not lst:
    print(-1)

else:
    print(sum(lst))
    print(lst[0])
