a, b, c, d = map(int, input().split())

s=[]
s.append((a+c)*max(b,d))
s.append((b+d)*max(a,c))
s.append(max(a,d)*(b+c))
s.append(max(b,c)*(a+d))

if min(s) == s[0]:
    print((a+c),max(b,d))
elif min(s) == s[1]:
    print((b+d),max(a,c))
elif min(s) == s[2]:
    print(max(a,d),(b+c))
else:
    print(max(b,c),(a+d))