direct = {'N': 0, 'S': 1, 'W': 2, 'E': 3, 'U': 4, 'D': 5}
rules = [[0] * 6 for _ in range(6)]
cnt_direct = 6

for i in range(cnt_direct):
    rule = input()
    for char in rule:
        rules[i][direct[char]] += 1

start, steps = input().split()
steps = int(steps)
dp = [[1] * cnt_direct for _ in range(steps + 1)]

for i in range(2, steps + 1):
    for j in range(cnt_direct):
        for k in range(cnt_direct):
            dp[i][j] += rules[j][k] * dp[i - 1][k]

print(dp[steps][direct[start]])
