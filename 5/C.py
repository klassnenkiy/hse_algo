n = int(input())
cities = set()
arr_x, arr_y = [], []

for _ in range(n):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)
    cities.add((x, y))

med_x = sorted(arr_x)[n // 2]
med_y = sorted(arr_y)[n // 2]

res = float('inf')
best_x, best_y = 0, 0

for x in range(med_x - 10, med_x + 11):
    for y in range(med_y - 10, med_y + 11):
        if (x, y) in cities:
            continue
        total = 0
        for cx, cy in zip(arr_x, arr_y):
            total += abs(cx - x) + abs(cy - y)
        if total < res:
            res = total
            best_x, best_y = x, y

print(best_x, best_y)
