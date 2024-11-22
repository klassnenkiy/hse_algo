n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in arr2:
    m = len(arr1) // 2
    l = 0
    r = len(arr1) - 1
    while arr1[m] != i and l <= r:
        if i > arr1[m]:
            l = m + 1
        else:
            r = m - 1
        m = (l + r) // 2

    if l > r:
        print('NO')
    else:
        print('YES')