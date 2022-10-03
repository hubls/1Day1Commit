n = int(input())

for i in range(n):
    num = int(input())
    lst = [0] * 101
    lst[1] = 1
    lst[2] = 1
    lst[3] = 1

    if num >= 4:
        for i in range(4, num + 1):
            lst[i] = lst[i-3] + lst[i-2]

    print(lst[num])

