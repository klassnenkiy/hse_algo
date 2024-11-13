a = int(input())
b = int(input())
n = int(input())
m = int(input())

min_t1 = n+a*(n-1)
min_t2 = m+b*(m-1)
max_t1 = n+a*(n+1)
max_t2 = m+b*(m+1)
min_t = max(min_t1, min_t2)
max_t = min(max_t1, max_t2)

if min_t > max_t:
    print(-1)
else:
    print(min_t,max_t)