n, k = map(int, input().split())
s = input()
res = n

for i in range(n - 1):
    j = 0
    b = k
    while (i - j >= 0) and (i + j + 1 < n) and (b or s[i - j] == s[i + j + 1]):
        res += 1
        if s[i - j] != s[i + j + 1]:
            b -= 1
        j += 1

for i in range(n - 1):
    j = 1
    b = k
    while (i - j >= 0) and (i + j < n) and (b or s[i - j] == s[i + j]):
        res += 1
        if s[i - j] != s[i + j]:
            b -= 1
        j += 1

print(res)