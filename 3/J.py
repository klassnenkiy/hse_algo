n = int(input())
l = list(map(int, input().split()))

while True:
    f = True
    for i in range(n):
        j = (i + 1) % n
        if l[j] >= l[i] + 2:
            print(l[j], l[i])
            l[i],l[j] = l[j],l[i]
            f = False
    if f:
        break

print(0)
