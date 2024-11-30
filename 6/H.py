n = int(input())
arr = []

for _ in range(n):
	open_hour,open_min,close_hour,close_min = map(int, input().split())
	open = open_hour * 60 + open_min
	close = close_hour * 60 + close_min
	if open >= close:
		arr.append((24 * 60, 1))
		arr.append((0, -1))
	arr.append((open, -1))
	arr.append((close, 1))

arr.sort()
cnt = 0
res = 0
for i in range(len(arr)):
	if cnt == n:
		res += arr[i][0] - arr[i - 1][0]
	if arr[i][1] == -1:
		cnt += 1
	else:
		cnt -= 1

print(res)
