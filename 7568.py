n = int(input())


lst = []

for i in range(n):
    a, b = input().split()
    lst.append([int(a), int(b)])


for i in range(n):
    weight = lst[i][0]
    height = lst[i][1]
    idx = 1
    for j in range(n):
        if weight >= lst[j][0] and height >= lst[j][1] :
            pass
        elif weight < lst[j][0] and height < lst[j][1]:
            idx += 1
    print(idx, end = " ")
