import sys

n = int(input())


lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline().strip()))

lst.sort()

for i in lst:
    print(i)
