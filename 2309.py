from itertools import combinations

lst = []
for i in range(9):
    n = int(input())
    lst.append(n)


res = list(combinations(lst,7))


lst2 = []
for l in res:
    if sum(l) == 100:
        lst2 = list(l)

lst2.sort()

for l in lst2:
    print(l)
