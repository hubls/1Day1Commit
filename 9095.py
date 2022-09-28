T = int(input())


for i in range(T):
    n = int(input())
    dp = [0] * (n + 1)

    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for j in range(4, n+1):
           dp[j] = dp[j-3] + dp[j-2] + dp[j-1]
        
        print(dp[n])

'''
틀린것들

from itertools import product

lst = [1,2,3]
idx = 0

n = int(input())


total = n
while(n > 0):
    for i in product(lst, repeat= n):
        if sum(i) == total and len(i) != 1 :
            idx += 1

    n -= 1
    

print(idx)





def plus(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return plus(n-3) + plus(n-2) + plus(n-1)


lst = []
for i in range(n):
    num = int(input())
    if num == 1:
        lst.append(0)
    elif num == 2:
        lst.append(1)
    elif num == 3:
        lst.append(3)
    else:
        lst.append(plus(num))


for i in lst:
    print(i)
'''
