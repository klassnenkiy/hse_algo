N=int(input())

for i in range(N):
    a1,b1,a2,b2,a3,b3,a4,b4 = map(int,input().split())
    if (a1-a4,b1-b4) == (a2-a3,b2-b3) or (a2-a3,b2-b3) == (a4-a1,b4-b1) \
        or (a2-a4,b2-b4) == (a3-a1,b3-b1) or (a3-a1,b3-b1)==(a4-a2,b4-b2):
        print('YES')
    else:
        print('NO')
