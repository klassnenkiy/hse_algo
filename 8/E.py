l, n = map(int, input().split())
arr = list(map(int, input().split()))

arr = [0] + arr + [l]
dp = [[0] * (n + 2) for _ in range(n + 2)]

for lens in range(2, n + 2):
    for i in range(n + 2 - lens):
        j = i + lens
        dp[i][j] = float('inf')
        for k in range(i + 1, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + (arr[j] - arr[i]))

print(dp[0][n + 1])
