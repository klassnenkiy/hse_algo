n, k = map(int, input().split())
l = list(map(int, input().split()))
deque = []
for i in range(n):
    if deque and deque[0] < i - k + 1:
        deque.pop(0)
    while deque and l[deque[-1]] > l[i]:
        deque.pop()
    deque.append(i)
    if i >= k - 1:
        print(l[deque[0]])
