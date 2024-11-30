g, n = map(int, input().split())
W = input()
S = input()

cnt1 = {}
for i in W:
    cnt1[i] = cnt1.get(i, 0) + 1
cnt2 = {}
for i in range(g):
    cnt2[S[i]] = cnt2.get(S[i], 0) + 1

res = 0
if cnt2 == cnt1:
    res += 1
for i in range(g, len(S)):
    l = S[i - g]
    cnt2[l] -= 1
    if cnt2[l] == 0:
        del cnt2[l]
    r = S[i]
    cnt2[r] = cnt2.get(r, 0) + 1
    if cnt2 == cnt1:
        res += 1

print(res)
