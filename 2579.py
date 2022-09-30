n = int(input())

total = [0] * 301
dp = [0] * 301

for i in range(n):
    total[i+1] = int(input())
    

dp[1] = total[1]
dp[2] = total[1] + total[2]
dp[3] = max(total[1] + total[3] , total[2] + total[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + total[i -1] + total[i], dp[i-2] + total[i])


print(dp[n])
