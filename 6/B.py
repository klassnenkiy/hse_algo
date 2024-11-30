n = int(input())
mounts = []
for _ in range(n):
	x, y = map(int, input().split())
	mounts.append(y)
m = int(input())
tracks = []
for _ in range(m):
	s, f = map(int, input().split())
	tracks.append((s, f))

r = [0]*n
l = [0]*n
for i in range(1, n):
	r[i] = r[i - 1] + max(mounts[i] - mounts[i - 1], 0)
	l[n - i - 1] = l[n - i] + max(mounts[n - i - 1] - mounts[n - i], 0)

for track in tracks:
	s, f = track[0] - 1, track[1] - 1
	if s < f:
		print(r[f] - r[s])
	else:
		print(l[f] - l[s])