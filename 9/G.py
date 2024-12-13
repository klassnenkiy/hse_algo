n,m = map(int, input().split())
s = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
dp = [[0]*(m + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(m + 1):
        dp[i][j] = dp[i - 1][j]
        if s[i] <= j:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - s[i]] + c[i])

print(max(dp[n]))
