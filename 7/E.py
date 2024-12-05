n, m = map(int, input().split())

dp = [[0] * m for i in range(n)]
dp[0][0] = 1
for i in range(1, n):
    for j in range(1, m):
        if i - 2 >= 0 and j - 1 >= 0:
            dp[i][j] += dp[i - 2][j - 1]
        if i - 1 >= 0 and j - 2 >= 0:
            dp[i][j] += dp[i - 1][j - 2]

print(dp[n - 1][m - 1])
