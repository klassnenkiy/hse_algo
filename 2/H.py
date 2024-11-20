n = int(input())

for _ in range(n):
    l = list(map(float, input().split()))
    k, conts = int(l[0]), l[1:]
    res = []
    queue = []
    for cont in conts:
        while queue and queue[-1] < cont:
            res.append(queue.pop())
        queue.append(cont)
    while queue:
        res.append(queue.pop())
    if res == sorted(res):
        print(1)
    else:
        print(0)
