def heap(arr, n, idx):
    j = idx
    l = (j * 2) + 1
    r = (j * 2) + 2
    if l < n and arr[l] > arr[j]:
        j = l
    if r < n and arr[r] > arr[j]:
        j = r
    if j != idx:
        arr[j], arr[idx] = arr[idx], arr[j]
        heap(arr, n, j)

def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heap(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)

n = int(input())
arr = list(map(int, input().split()))
heap_sort(arr)
print(*arr)
