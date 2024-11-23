w, h, n = map(int, input().split())

l = max(w, h)
r = n * l
while l < r:
    mid = (l + r) // 2
    if (mid // w) * (mid // h) >= n:
        r = mid
    else:
        l = mid + 1

print(l)
