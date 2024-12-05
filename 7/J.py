m, n = map(int, input().split())
if n == 0:
    print("")
    exit()

word_lens = list(map(int, input().split()))


dp = [float('inf')] * (n + 1)
dp[0] = 0
prev = [-1] * (n + 1)

for i in range(n):
    lens = 0
    for j in range(i, n):
        lens += word_lens[j]
        if j > i:
            lens += 1
        if lens > m:
            break
        spaces = m - lens
        penalty = spaces ** 3
        if dp[j + 1] > dp[i] + penalty:
            dp[j + 1] = dp[i] + penalty
            prev[j + 1] = i
        elif dp[j + 1] == dp[i] + penalty and prev[j + 1] < i:
            prev[j + 1] = i

res = []
i = n
while i > 0:
    start = prev[i]
    res.append(i - start)
    i = start

res.reverse()

print(" ".join(map(str, res)))
