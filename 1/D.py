n,k,m = map(int, input().split())

c = 0
while n >= k and k >=m:
    c += (n//k) * (k // m)
    n = n%k + (n//k)*(k % m)

print(c)