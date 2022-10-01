from itertools import combinations

n, r = map(int, input().split())
arr = list(range(1, n+1))
nCr = list(combinations(arr, r))
nCr.sort()



for i in range(len(nCr)):
    for j in range(len(nCr[i])):
        print(nCr[i][j], end = ' ')

    print()
