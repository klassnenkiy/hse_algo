n = int(input())
if n == 0:
    print()
else:
    l=list(map(int, input().split()))
    max_idx = 0

    for i in range(1, len(l)):
        if l[i] > l[max_idx]:
            max_idx = i
    l[-1], l[max_idx] = l[max_idx], l[-1]
    print(*l)