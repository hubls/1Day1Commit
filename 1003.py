'''
def fibonacci(n):
    if n == 0 :
        global idx0
        idx0 += 1
        
        return 0
    elif n == 1 :
        global idx1
        idx1 += 1
        
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

'''

n = int(input())

for i in range(n):
    idx0 = 0
    idx1 = 0
    num = int(input())
    dp0 = [0] * (num + 1)
    dp1 = [0] * (num + 1)
    
    if num == 0:
        dp0[0] = 1
        dp1[0] = 0
    elif num == 1 :
        dp0[1] = 0
        dp1[1] = 1
    else:
        dp0[0] = 1
        dp0[1] = 0
        dp1[0] = 0
        dp1[1] = 1
        for i in range(2, num+1):
            dp0[i] = dp0[i-2] + dp0[i-1]
            dp1[i] = dp1[i-2] + dp1[i-1]
        
    print(dp0[num], dp1[num])

