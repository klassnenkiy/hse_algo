#1 version

n = int(input())
l =list(map(int, input().split()))

g = []
loosers = []
strength = l[0]

for i in range(1, n):
    g.append((strength, l[i]))
    if strength < l[i]:
        loosers.append(strength)
        strength= l[i]
    else:
        loosers.append(l[i])
for i in range(int(input())):
    k = int(input())
    if k <= len(g):
        print(*g[k-1])
    else:
        print(strength,loosers[(k-len(g) -1) % len(loosers)])


# 2 version

from collections import deque

n = int(input())
l = deque(map(int, input().split()))
max_strength = max(l)
pairs = []
g = 0

for i in range(n):
    first = l[0]
    second = l[1]
    pairs += [(first, second)]
    g += 1
    if first < second:
        l.append(l.popleft())
    else:
        l[0],l[1] = l[1],l[0]
        l.append(l.popleft())
l.popleft()
for i in range(int(input())):
    k = int(input())
    if k <= g:
        print(pairs[k-1][0], pairs[k-1][1])
    else:
        print(max_strength, l[(k-g-1) % (n-1)])
