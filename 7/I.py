from bisect import bisect_right

n = int(input())
intrvls = []
for _ in range(n):
    b, e, w = map(float, input().split())
    intrvls.append((b, e, w))

intrvls.sort(key=lambda x: x[1])

s = [interval[0] for interval in intrvls]
end = [interval[1] for interval in intrvls]
w = [interval[2] for interval in intrvls]

dp = [0] * (len(intrvls) + 1)

for i in range(1, len(intrvls)+1):
    j = bisect_right(end, s[i-1]) - 1
    dp[i] = max(dp[i-1], w[i-1] + dp[j+1])

print(f'{dp[-1]:.4f}')
