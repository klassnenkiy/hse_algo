n, m = map(int, input().split())
s = [0] + list(map(int, input().split()))
dp = [[False] * (m + 1) for i in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
    for j in range(m + 1):
        dp[i][j] = dp[i - 1][j]
        if s[i] <= j and dp[i - 1][j - s[i]]:
            dp[i][j] = True

res = []
for i in range(m + 1):
    if dp[n][i]:
        res.append(i)

print(max(res))
