n, m = map(int, input().split())
arr = []
for _ in range(m):
	b, e = map(int, input().split())
	arr.append((b,-1))
	arr.append((e,1))

arr.sort()
tch = 0
res = n
for i in range(len(arr)):
	if tch:
		res -= arr[i][0] - arr[i - 1][0]
	if arr[i][1] == -1:
		tch += 1
	elif arr[i][1] == 1:
		tch -= 1
		if tch == 0:
			res -= 1

print(res)
