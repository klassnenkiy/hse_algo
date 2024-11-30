mods = [10**9 + 7, 10**9 + 11, 10**9 + 13]
max_fib_idx = 24501
fib_mod_sets = []
for _ in range(len(mods)):
    fib_mod_sets.append(set())

for idx in range(len(mods)):
    f1, f2 = 1, 1
    fib_mod_sets[idx].add(1)
    for _ in range(max_fib_idx):
        f1, f2 = f2, (f1 + f2) % mods[idx]
        fib_mod_sets[idx].add(f2)

qs = []
n = int(input())
for i in range(n):
    qs.append(input().strip())

res = []
for q in qs:
    is_fib = True
    for mod_idx, mod in enumerate(mods):
        curr_mod = 0
        for c in q:
            curr_mod = (curr_mod * 10 + int(c)) % mod
        if curr_mod not in fib_mod_sets[mod_idx]:
            is_fib = False
            break
    if is_fib:
        res.append('Yes')
    else:
        res.append('No')

print('\n'.join(res))
