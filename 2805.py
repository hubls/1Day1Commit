import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))


start = 0
end = max(tree)

while(start <= end):
    mid = (start + end) // 2
    total = 0
    for t in tree:
        if t > mid:
            total += t - mid
    if total >= m :
        start = mid + 1
        
    else: 
        end = mid -1

            
print(end)
