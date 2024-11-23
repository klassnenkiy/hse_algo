def add(heap, val):
    heap.append(val)
    pos = len(heap) - 1
    while pos > 0 and heap[pos] > heap[(pos - 1) // 2]:
        heap[pos], heap[(pos - 1) // 2] = heap[(pos - 1) // 2], heap[pos]
        pos = (pos - 1) // 2


def delet(heap):
    max_val = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    pos = 0
    while pos * 2 + 1 < len(heap):
        largest_child = pos * 2 + 1
        if pos * 2 + 2 < len(heap) and heap[pos * 2 + 2] > heap[largest_child]:
            largest_child = pos * 2 + 2
        if heap[pos] < heap[largest_child]:
            heap[pos], heap[largest_child] = heap[largest_child], heap[pos]
            pos = largest_child
        else:
            break
    return max_val


heap = []
for _ in range(int(input())):
    cmd = input()
    if cmd == '1':
        print(delet(heap))
    else:
        val = int(cmd.split()[1])
        add(heap, val)
