n = int(input())
l = list(map(int, input().split()))

s = set()
res = []
for i in range(n - 1,-1,-1):
    if l[i] not in s:
        s.add(l[i])
        res.append(l[i])
print(len(res))
print(*res[::-1])