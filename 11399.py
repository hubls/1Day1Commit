import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()


total = 0
for i in range(n):
    for j in range(i+1):
        total += lst[j]

print(total)
