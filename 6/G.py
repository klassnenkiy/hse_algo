n, m = map(int, input().split())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((min(a,b), 1))
    arr.append((max(a,b), 3))

coords = list(map(int, input().split()))
for coord in set(coords):
    arr.append((coord, 2))

arr.sort()
cnt = {i: 0 for i in coords}
cntseg = 0
for seg in arr:
    if seg[1] == 1:
        cntseg += 1
    if seg[1] == 2:
        cnt[seg[0]] = cntseg
    if seg[1] == 3:
        cntseg -= 1

for i in range(m):
    print(cnt[coords[i]], end=' ')
