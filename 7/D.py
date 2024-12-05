n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[0][0] = g[0][0]

for j in range(1, m):
    dp[0][j] = dp[0][j - 1] + g[0][j]
for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + g[i][0]
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = g[i][j] + min(dp[i - 1][j], dp[i][j - 1])

res = dp[n - 1][m - 1]
coords = []
i, j = n - 1, m - 1
while i > 0 or j > 0:
    coords.append((i + 1, j + 1))
    if i > 0 and dp[i - 1][j] <= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1
coords.append((1, 1))
coords.reverse()
print(res)
print(len(coords))
for c in coords:
    print(*c)
