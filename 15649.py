from itertools import permutations

n, r = map(int, input().split())
arr = list(range(1, n+1))
nPr = list(permutations(arr,r))




for i in range(len(nPr)):
    for j in range(len(nPr[i])):
        print(nPr[i][j], end = ' ')

    print()
