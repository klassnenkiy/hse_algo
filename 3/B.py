n = int(input())
if n == 0:
    print()
else:
    l = list(map(int, input().split()))
    for i in range(n-1,-1,-1):
        max_idx = i
        for j in range(i-1,-1,-1):
            if l[j] > l[max_idx]:
                max_idx = j
        l[max_idx],l[i] = l[i],l[max_idx]
    print(*l)
