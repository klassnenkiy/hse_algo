m, n = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    for j in range(m):
        dp[i + 1][j] += dp[i][j]
        dp[i][j + 1] += dp[i][j]
        dp[i + 1][j + 1] += dp[i][j]

print(dp[n - 1][m - 1])
