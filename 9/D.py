k = int(input())
a = list(map(int, input().split()))
b = [i for i in range(k)]
dp = [[0] * k for _ in range(k)]

for i in range(k - 1):
    dp_a, dp_b = zip(*sorted(zip(a, b)))
    dp_a, dp_b = list(dp_a), list(dp_b)

    for j in range(i + 1, k):
        if dp[dp_b[i]][dp_b[j]] > 0:
            continue
        elif dp_a[i] > 0:
            dp[dp_b[i]][dp_b[j]] = 1
            dp[dp_b[j]][dp_b[i]] = 1
            dp_a[i] -= 1
            a[dp_b[j]] -= 1
        elif dp_a[i] == 0:
            dp[dp_b[j]][dp_b[i]] = 2
            a[dp_b[j]] -= 2

    a[dp_b[i]] = -i - 1

for i in range(k):
    print(*dp[i])
