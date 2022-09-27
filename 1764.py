import sys

n, m = map(int, input().split())

set1 = set()
set2 = set() 

for i in range(n):
    set1.add(sys.stdin.readline().rstrip())

for j in range(m):
    set2.add(sys.stdin.readline().rstrip())



inter = list(set1 & set2)


inter.sort()

print(len(inter))
for i in inter:
    print(i)
