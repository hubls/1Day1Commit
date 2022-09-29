n = int(input())


lst = [0] * (n+1)

if n == 1:
    print(1)

elif n == 2:
    print(2)

else:
    lst[1] = 1
    lst[2] = 2
    for i in range(3, n+1):
        lst[i] = lst[i-1] + lst[i-2]
    print(lst[n]%10007)   

