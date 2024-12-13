N, M = map(int, input().split())
n = sorted((int(x) + 1, i) for i, x in enumerate(input().split()))
m = sorted((int(y), j) for j, y in enumerate(input().split()))

g = 0
a = 0
dist = [0] * len(n)

while g < len(n) and a < len(m):
    g_sz, g_idx = n[g]
    a_sz, a_idx = m[a]
    if g_sz <= a_sz:
        dist[g_idx] = a_idx + 1
        g += 1
    a += 1

print(g)
print(*dist)
