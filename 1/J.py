k = [list(map(int, input().split())) for _ in range(3)]
x_cnt = sum(row.count(1) for row in k)
o_cnt = sum(row.count(2) for row in k)

if x_cnt != o_cnt and x_cnt != o_cnt + 1:
    print('NO')
else:
    x_win = False
    o_win = False
    for i in range(3):
        # чек строк
        if k[i][0] == k[i][1] == k[i][2]:
            if k[i][0] == 1:
                x_win = True
            elif k[i][0] == 2:
                o_win = True

        # чек столбцов
        if k[0][i] == k[1][i] == k[2][i]:
            if k[0][i] == 1:
                x_win = True
            elif k[0][i] == 2:
                o_win = True

    # чек диагоналей
    if k[0][0] == k[1][1] == k[2][2]:
        if k[0][0] == 1:
            x_win = True
        elif k[0][0] == 2:
            o_win = True

    if k[0][2] == k[1][1] == k[2][0]:
        if k[0][2] == 1:
            x_win = True
        elif k[0][2] == 2:
            o_win = True

    if x_win and o_win:
        print('NO')
    elif x_win and x_cnt != o_cnt + 1:
        print('NO')
    elif o_win and x_cnt != o_cnt:
        print('NO')
    else:
        print('YES')
