import sys
import math

def distance(x1, y1, x2, y2):
    result = math.sqrt(math.pow(x1 - x2, 2) + math.pow((y1 - y2), 2))
    return result

n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = distance(x1, y1, x2, y2)
    tmp = r1
    r1 = min(r1, r2)
    r2 = max(tmp, r2)

    if d == 0 and r1 == r2:
        print(-1)

    elif r1 + r2 == d or r2 - r1 == d :
        print(1)

    elif r2 - r1 < d < r1 + r2 :
        print(2)
    else:
        print(0)




