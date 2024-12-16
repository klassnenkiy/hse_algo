def get_hash(s):
    res = 0
    for i in s:
        res = (res + ord(i)) % 128
    return res


n = int(input())
s = 'dd'
for i in range(n):
    print(s)
    s += 'dd'