def foo(i, j):
    if 0 <= i < n and 0 <= j < m:
        if dp[i][j] == -1:
            dp[i][j] = foo(i-2,j-1)+foo(i-2,j+1)+foo(i-1,j-2)+foo(i+1,j-2)
    else:
        return 0
    return dp[i][j]

n,m = map(int, input().split())
dp = [[-1] * m for i in range(n)]
dp[0][0] = 1

print(foo(n - 1, m - 1))
