def solve():
    N, K = map(int, input().split())
    bricks = []

    color_to_bricks = [[] for _ in range(K + 1)]

    for i in range(N):
        L, C = map(int, input().split())
        bricks.append((L, C, i + 1))
        color_to_bricks[C].append((L, i + 1))

    max_length = sum(L for L, C, _ in bricks)
    def can_make_layer(color_bricks, target_length):
        b = [False] * (target_length + 1)
        b[0] = True

        for length, _ in color_bricks:
            for t in range(target_length, length - 1, -1):
                if b[t - length]:
                    b[t] = True
        return b[target_length]

    can = [True] * (max_length + 1)
    can[0] = False

    for color in range(1, K + 1):
        color_bricks = color_to_bricks[color]
        target_length = sum(length for length, _ in color_bricks)

        if not can_make_layer(color_bricks, target_length):
            print("NO")
            return

        b = [False] * (max_length + 1)
        b[0] = True
        for length, _ in color_bricks:
            for t in range(max_length, length - 1, -1):
                if b[t - length]:
                    b[t] = True

        for j in range(max_length + 1):
            can[j] = can[j] and b[j]

    f = False
    for i in range(max_length, 0, -1):
        if can[i]:
            f = True
            v = i
            break

    if f:
        print("YES")
        print(v)
    else:
        print("NO")


solve()
