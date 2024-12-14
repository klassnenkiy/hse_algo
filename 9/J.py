# не решил
n, k = map(int, input().split())
b = []
for i in range(n):
    Li, Ci = map(int, input().split())
    b.append((Li, Ci - 1))

clr_b = [[] for _ in range(k)]
for idx, (Li, Ci) in enumerate(b):
    clr_b[Ci].append((Li, idx + 1))

max_len = sum(Li for Li, _ in b)

dp = [[False] * (max_len + 1) for _ in range(k)]
dp[0][0] = True

for clr in range(k):
    for Li, _ in clr_b[clr]:
        for j in range(max_len, Li - 1, -1):
            if dp[clr][j - Li]:
                dp[clr][j] = True

for v in range(1, max_len):
    f = True
    for clr in range(k):
        if not dp[clr][v]:
            f = False
            break
    if f:
        print('YES')

        wall_1 = []
        remain_len = v
        for clr in range(k - 1, -1, -1):
            for Li, idx in reversed(clr_b[clr]):
                if remain_len >= Li and dp[clr][remain_len - Li]:
                    wall_1.append(idx)
                    remain_len -= Li
                    break

        print(*sorted(wall_1))
        exit()

print('NO')
