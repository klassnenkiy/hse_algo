import math

N=int(input())
l=list(map(int, input().split()))
print(math.ceil(sum(l)/N))