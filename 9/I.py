n = int(input())
a,b,c = map(int, input().split())
floors = [0] * (n + 1)
floors[1] = 1

for i in range(n, -1, -1):
    if floors[i] == 1:
        if i + b <= n:
            floors[i + b] = 1

for j in range(3):
    if j == 0:
        delta = a
    elif j == 1:
        delta = b
    elif j == 2:
        delta = c

    for i in range(n + 1):
        if floors[i] == 1:
            if i + delta <= n:
                floors[i + delta] = 1

print(sum(floors))
