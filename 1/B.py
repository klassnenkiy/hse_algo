a, b, c = int(input()), int(input()), int(input())

if a == 0 and b == c**2:
    print('MANY SOLUTIONS')
elif c < 0 or (a == 0 and b != c**2):
    print('NO SOLUTION')
else:
    if (c**2 - b)/a == int((c**2 - b)/a):
        print(int((c**2 - b)/a))
    else:
        print('NO SOLUTION')