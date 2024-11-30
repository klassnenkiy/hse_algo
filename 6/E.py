k = int(input())
s = input()

c = 0
res = 0

for i in range(len(s) - k - 1,-1,-1):
    if s[i] == s[i+k]:
        c += 1
    else:
        c = 0
    res += c

print(res)
