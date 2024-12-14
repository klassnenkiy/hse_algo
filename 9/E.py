# не решил
import bisect

n = int(input())
sts = []
for i in range(n):
    h, l = map(int, input().split())
    sts.append((h + l, h, i + 1))
H = int(input())

sts.sort()
saved = []
max_h = -1
res = []

for total_height, height, st_num in sts:
    if total_height >= H:
        res.append(st_num)
        max_h = max(max_h, height)
        saved.append(height)
    else:
        if saved and height < max_h:
            idx = bisect.bisect_right(saved, height)
            if idx > 0:
                saved[idx - 1] = height
                res.remove(saved[idx - 1])
                res.append(st_num)
                max_h = max(saved)

print(len(res))
if res:
    print(*res)
