n = input()

idx = 0

if len(n) <= 2:
    print(n)

elif len(n) >= 3:
    idx = 99
    for i in range(100, int(n)+1):
        i = str(i)
        lst = []
        for j in range(2):
            lst.append(int(i[j+1]) - int(i[j]))

        if lst[0] == lst[1]:
            idx +=1
    print(idx)
