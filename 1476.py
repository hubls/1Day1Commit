import sys

e, s, m = map(int, sys.stdin.readline().split())

count = 1
e1, s1, m1 = 1, 1, 1

while(e1 != e or s1 != s or m1 != m):
    count += 1
    e1 += 1
    s1 += 1
    m1 += 1
    if e1 > 15:
        e1 = 1
    if s1 > 28 :
        s1 = 1
    if m1 > 19 :
        m1 = 1


print(count)