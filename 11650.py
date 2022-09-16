import sys

n = int(input())

lst = []

for i in range(n):
    data =list(map(int, sys.stdin.readline().split()))
    lst.append(data)


lst.sort(key = lambda x:(x[0], x[1]))

for i in range(n):
    print(lst[i][0], lst[i][1])

