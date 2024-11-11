N, i, j = map(int, input().split())

print(min(abs(j-i)-1,N-abs(i-j) - 1))