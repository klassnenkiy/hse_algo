cmd = input()
deque = []
while cmd != 'exit':
    if 'push_front' in cmd:
        pussh, n = cmd.split()
        deque.insert(0,n)
        print('ok')
    elif 'push_back' in cmd:
        pussh, n = cmd.split()
        deque.append(n)
        print('ok')
    elif 'pop_front' in cmd:
        if deque:
            print(deque.pop(0))
        else:
            print('error')
    elif 'pop_back' in cmd:
        if deque:
            print(deque.pop())
        else:
            print('error')
    elif 'front' in cmd:
        if deque:
            print(deque[0])
        else:
            print('error')
    elif 'back' in cmd:
        if deque:
            print(deque[-1])
        else:
            print('error')
    elif 'size' in cmd:
        print(len(deque))
    elif 'clear' in cmd:
        deque.clear()
        print('ok')
    cmd = input()

print('bye')
