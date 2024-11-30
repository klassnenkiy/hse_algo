n = int(input())
s = input()
d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

mid = ''
s = ''
for i in sorted(d):
    s += i * (d[i] // 2)
    if d[i] % 2 == 1 and mid == '':
        mid = i

print(s + mid + s[::-1])
