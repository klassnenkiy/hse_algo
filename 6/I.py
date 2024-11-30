n = int(input())
arr = []

for i in range(n):
    t, l = map(int, input().split())
    s = t + l
    arr.append((t, 1))
    arr.append((s, -1))

arr.sort()
c = 0
max_c = 0

for i in range(len(arr)):
    if arr[i][1] == 1:
        c += 1
        max_c = max(c, max_c)
    if arr[i][1] == -1:
        c -= 1

print(max_c)
