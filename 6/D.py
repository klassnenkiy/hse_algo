n, k = map(int, input().split())
s = input()
d = dict.fromkeys(s, 0)
i,j,l,r = 0,0,0,0

while j < n:
    if d[s[j]] < k:
        if j - i > r - l:
            r, l = j, i
        d[s[j]] += 1
        j += 1
    else:
        i = j - k + 1
        d = dict.fromkeys(d.keys(), 0)
print(r - l + 1,l + 1)