s = input()
q = int(input())
for i in range(q):
    l, a, b = map(int, input().split())
    f = True
    for j in range(l):
        if s[a + j] > s[b + j]:
            f = False
            print(1)
            break
        elif s[a + j] < s[b + j]:
            f = False
            print(-1)
            break
    if f:
        print(0)
