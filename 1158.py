import sys

n, k = map(int, sys.stdin.readline().split())

lst = list(range(1, n+1))
outputlst = []

idx = 0

for i in range(n):
    idx += k-1

    if idx >= len(lst):
        idx = idx % len(lst)

    outputlst.append(lst.pop(idx))
    

print("<", end = '')
for i in range(len(outputlst)):
    
    if i == len(outputlst)-1:
        print(outputlst[i], end ='')
    else:
        print(outputlst[i], end = ', ')

print(">", end ='')
