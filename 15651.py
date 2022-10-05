import itertools


n, k = map(int, input().split())

lst = list(range(1,n+1))

nPr = list(itertools.product(lst, repeat=k))

for l in nPr:
    for j in l:
        print(j, end = ' ')

    print()
