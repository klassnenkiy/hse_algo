fath = input()
moth = input()

f_arr = [0] * 26
m_arr = [0] * 26

for i in fath:
    f_arr[ord(i) - ord('a')] += 1
for i in moth:
    m_arr[ord(i) - ord('a')] += 1

f = 0
m = 0
res = []

for max_symb in range(ord('z'), ord('a') - 1, -1):
    while f_arr[max_symb - ord('a')] > 0 and m_arr[max_symb - ord('a')] > 0:
        res.append(chr(max_symb))
        while fath[f] != chr(max_symb):
            f_arr[ord(fath[f]) - ord('a')] -= 1
            f += 1
        f_arr[max_symb - ord('a')] -= 1
        f += 1
        while moth[m] != chr(max_symb):
            m_arr[ord(moth[m]) - ord('a')] -= 1
            m += 1
        m_arr[max_symb - ord('a')] -= 1
        m += 1

print(''.join(res))
