n = int(input())
arr = list(map(int, input().split()))
x = int(input())
i = 0

for j in range(n):
  if arr[j] < x:
    arr[i],arr[j] = arr[j],arr[i]
    i += 1

print(i)
print(n-i)
