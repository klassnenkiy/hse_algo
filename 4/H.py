def bin_s(seq1, seq2, l):
    n = 2*l
    center = (n + 1)// 2
    low = 0
    high = l
    while low <= high:
        mid1 = (low + high)// 2
        mid2 = center - mid1
        left1 = seq1[mid1 - 1] if mid1 > 0 else float('-inf')
        right1 = seq1[mid1] if mid1 < l else float('inf')
        left2 = seq2[mid2 - 1] if mid2 > 0 else float('-inf')
        right2 = seq2[mid2] if mid2 < l else float('inf')
        if left1 <= right2 and left2 <= right1:
            return max(left1, left2)
        if left1 > right2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0


n, l = map(int, input().split())
arr = []

for _ in range(n):
    x1, d1, a, c, m = map(int, input().split())
    seq = []

    for i in range(l):
        seq.append(x1)
        x1 = x1 + d1
        d1 = (a * d1 + c) % m

    arr.append(seq)

for i in range(n - 1):
    for j in range(i + 1, n):
        seq1 = arr[i]
        seq2 = arr[j]
        print(bin_s(seq1, seq2, l))
