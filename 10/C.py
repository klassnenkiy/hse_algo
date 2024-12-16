def pref_foo(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

s = input()
n = len(s)
pi = pref_foo(s)
min_len = n - pi[-1]
print(min_len)



