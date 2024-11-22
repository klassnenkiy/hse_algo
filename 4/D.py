n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

d = {}

for i in range(n):
    k = arr1[i]
    if k not in d:
        d[k] = [i + 1, i + 1]
    else:
        d[k][1] = i + 1
for i in arr2:
    if i in d:
        print(*d[i])
    else:
        print(0, 0)


n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

for x in arr2:
    l, r = 0, n - 1
    l_res = -1
    while l <= r:
        m = (l + r) // 2
        if arr1[m] == x:
            l_res = m
            r = m - 1
        elif arr1[m] < x:
            l = m + 1
        else:
            r = m - 1

    l, r = 0, n - 1
    r_res = -1
    while l <= r:
        m = (l + r) // 2
        if arr1[m] == x:
            r_res = m
            l = m + 1
        elif arr1[m] < x:
            l = m + 1
        else:
            r = m - 1


    if l_res != -1:
        print(l_res + 1, r_res + 1)
    else:
        print(0, 0)
