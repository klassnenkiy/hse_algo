n, r = map(int, input().split())
d = list(map(int, input().split()))

i = 0
j = 1
res = 0

while j < n and i < n - 1:
    if d[j] - d[i] <= r:
        j += 1
    else:
        res += n - j
        i += 1

print(res)
