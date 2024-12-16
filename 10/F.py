def get_hash(r, ln, d):
    return (d[r + ln - 1] - d[r - 1] * z[ln]) % (10 ** 9 + 7)

n, m = map(int, input().split())
m += 1
colors = list(map(int, input().split()))

colors_prefix = [0] * (n + 1)
reversed_colors_prefix = [0] * (n + 1)
z = [1] * (n + 1)

for i in range(1, n + 1):
    colors_prefix[i] = (colors_prefix[i - 1] * m + colors[i - 1]) % (10 ** 9 + 7)
    reversed_colors_prefix[i] = (reversed_colors_prefix[i - 1] * m + colors[n - i]) % (10 ** 9 + 7)
    z[i] = (z[i - 1] * m) % (10 ** 9 + 7)

res = []

for i in range(n // 2 + 1):
    if get_hash(n - i + 1, i, reversed_colors_prefix) == get_hash(i + 1, i, colors_prefix):
        res.append(n - i)

print(*res[::-1])
