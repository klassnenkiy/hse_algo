def compute_A(n, s):
    res = []
    for i in range(1, n+1):
        k = 0
        while k < i and s[k] == s[i-k-1]:
            k += 1
        res.append(k)
    return res

n = int(input())
s = input()

res = compute_A(n, s)

print(' '.join(map(str, res)))
