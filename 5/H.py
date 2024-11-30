from collections import Counter

a = input()
b = input()
sa, sb = set(a), set(b)
num = sorted(sa.intersection(sb), reverse=True)

if len(num)!=0:
    da = Counter(a)
    db = Counter(b)
    res = ''
    for i in num:
        res += i * min(db.get(i, 0), da.get(i, 0))
    if not res:
        print('-1')
    elif res[0] == '0':
        print('0')
    else:
        print(res)
else:
    print('-1')
