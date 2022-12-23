n = int(input())

k = 0

count = 0

while True :
    count += 1
    k += count
    if k == n :
        break
    elif k > n :
        count = count - 1
        break

print(count)