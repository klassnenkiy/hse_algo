n = int(input())
arr1 = list(map(int, input().split()))
k = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    arr1[i-1] -= 1
for i in range(n):
    if arr1[i] < 0:
        print('yes')
    else:
        print('no')
