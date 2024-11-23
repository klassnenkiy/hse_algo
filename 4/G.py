n = int(input())

diag = (int(((8*n - 7) ** 0.5) - 1) // 2) + 1
pos = n - (diag * (diag - 1) // 2)

if diag % 2 == 0:
    print(f"{diag - pos + 1}/{pos}")
else:
    print(f"{pos}/{diag - pos + 1}")