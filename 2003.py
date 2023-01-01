import sys
n, m = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))


start, end = 0, 1
cnt = 0

while end <= n and start <= end:

    total = sum(lst[start:end])

    if total < m :
        end += 1

    elif total > m :
        start += 1

    else:
        cnt += 1
        end += 1


print(cnt)
