n,k,s = map(int, input().split())

unit_grid = [[0] * k for _ in range(k)]
for idx in range(s):
    r = idx // k
    c = idx % k
    unit_grid[r][c] = 1

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dp[i][j] = unit_grid[i % k][j % k]

for r in dp:
    print(' '.join(map(str, r)))
