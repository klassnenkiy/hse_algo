N = int(input())
dp = [0] * (N + 1)
p = [-1] * (N + 1)

for i in range(2, N + 1):
    min_op = 10**6
    if i % 3 == 0:
        min_op = dp[i // 3]
    if i % 2 == 0:
        min_op = min(min_op, dp[i // 2])
    min_op = min(dp[i - 1], min_op)
    dp[i] = min_op + 1
    if i % 3 == 0 and dp[i // 3] == min_op:
        p[i] = i // 3
    elif i % 2 == 0 and dp[i // 2] == min_op:
        p[i] = i // 2
    else:
        p[i] = i - 1

print(dp[N])

ans = [N]
i = N

while i != 1:
    ans += [p[i]]
    i = p[i]

print(*ans[::-1])
