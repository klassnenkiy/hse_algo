s = input()
n = len(s)
INF = 10**13

dp_split = [[-1] * n for _ in range(n)]
dp_loss = [[INF] * n for _ in range(n)]

for i in range(n):
    dp_split[i][i] = i
    dp_loss[i][i] = 1
    if i - 1 >= 0:
        dp_loss[i][i - 1] = 0

for length in range(1, n):
    for i in range(0, n - length):
        j = i + length
        if ((s[i] == "(" and s[j] == ")") or
                (s[i] == "[" and s[j] == "]") or
                (s[i] == "{" and s[j] == "}")):
            dp_loss[i][j] = dp_loss[i + 1][j - 1]

        for k in range(i, j):
            c_loss = dp_loss[i][k] + dp_loss[k + 1][j]
            if c_loss < dp_loss[i][j]:
                dp_loss[i][j] = c_loss
                dp_split[i][j] = k

def get_valid(s, dp_split, range_key):
    if range_key[1] - range_key[0] <= 0:
        return ""
    elif dp_split[range_key[0]][range_key[1]] == -1:
        return s[range_key[0]] + get_valid(s, dp_split, (range_key[0] + 1, range_key[1] - 1)) + s[range_key[1]]
    else:
        return (get_valid(s, dp_split, (range_key[0], dp_split[range_key[0]][range_key[1]])) +
                get_valid(s, dp_split, (dp_split[range_key[0]][range_key[1]] + 1, range_key[1])))

range_key = (0, n - 1)
print(get_valid(s, dp_split, range_key))
