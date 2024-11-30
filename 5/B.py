def quick_sort(arr, l, r):
    while l < r:
        i,j = l,r
        x = arr[(l + r) // 2]
        while i <= j:
            while arr[i] < x:
                i += 1
            while arr[j] > x:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        if j - l < r - i:
            quick_sort(arr, l, j)
            l = i
        else:
            quick_sort(arr, i, r)
            r = j

n = int(input())
arr = list(map(int, input().split()))
quick_sort(arr, 0, n - 1)
print(*arr)
