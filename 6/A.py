n = int(input())
arr = list(map(int, input().split()))

p_sum = [0]*(len(arr))
p_sum[0] = arr[0]
for i in range(1, len(p_sum)):
    p_sum[i] = max(p_sum[i-1], 0) + arr[i]

print(max(p_sum))
