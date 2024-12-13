def recover_items(n, max_weight):
    global max_value
    items = []
    while n > 0 and max_weight > 0:
        remain_weight = max_weight - w[n - 1]
        if dp[n - 1][max_weight] != dp[n][max_weight]:
            items.append(n)
            n -= 1
            max_weight = remain_weight
            max_value = dp[n][max_weight]
        else:
            n -= 1
    return items

n, m = map(int, input().split())
w = list(map(int, input().split()))
val = list(map(int, input().split()))

dp = [[-1] * (m + 1)]
dp[0][0] = 0
for i in range(n):
    dp.append([0] * (m + 1))
    for j in range(m + 1):
        dp[-1][j] = dp[-2][j]
    for j in range(m - w[i], -1, -1):
        if dp[-1][j] != -1 and dp[-1][j + w[i]] < dp[-1][j] + val[i]:
            dp[-1][j + w[i]] = dp[-1][j] + val[i]

max_value = max(dp[-1])
pos = 0
for i in range(len(dp[-1])):
    if dp[-1][i] == max_value:
        pos = i
items = recover_items(n, pos)

print(*items[::-1], sep='\n')
