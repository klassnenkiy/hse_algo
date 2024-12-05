n = int(input())
dp = [2, 4, 7]
for i in range(3, n+1):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

print(dp[n-1])
