from itertools import combinations

lst =[1]
while True:
    lst = list(map(int, input().split()))
    if lst.pop(0) == 0:
        break

    comb = list(combinations(lst, 6))
    comb.sort()
    for i in comb :
        for j in i:
            print(j, end=' ')
        print()
    print()
