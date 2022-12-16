n = int(input())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_a.sort()
list_b.sort()

total = 0

for i in range(n):
    total += list_a[i] * list_b[n -i -1]

print(total)