cmd = input()
queue = []
while cmd != 'exit':
    if 'push' in cmd:
        pussh, n = cmd.split()
        queue.append(n)
        print('ok')
    elif 'pop' in cmd:
        if queue:
            print(queue.pop(0))
        else:
            print('error')
    elif 'front' in cmd:
        if queue:
            print(queue[0])
        else:
            print('error')
    elif 'size' in cmd:
        print(len(queue))
    elif 'clear' in cmd:
        queue.clear()
        print('ok')
    cmd = input()

print('bye')
