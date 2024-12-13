m = int(input())
dp = list(map(int, input().split()))

s = 0
for i in range(1, 31):
    if dp[i - 1] * 2 > dp[i]:
        dp[i] = dp[i - 1] * 2

for i in range(30, -1, -1):
    if dp[i] <= m:
        m = m - dp[i]
        s = s + 2 ** i

if m > 0:
    s += 1

print(s)
