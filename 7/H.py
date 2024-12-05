n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
for i in range(1, len(arr)):
    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

m = max(dp)
res = []
i = n - 1
while m > 0:
    if dp[i] == m:
        res.append(arr[i])
        m -= 1
    i -= 1

print(*res[::-1])
