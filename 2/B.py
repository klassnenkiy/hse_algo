stack = []
cmd = input()

while cmd != 'exit':
    if 'push' in cmd:
        pussh, n = cmd.split()
        stack.append(n)
        print('ok')
    elif 'pop' in cmd:
        if stack:
            print(stack.pop())
        else:
            print('error')
    elif 'back' in cmd:
        if stack:
            print(stack[-1])
        else:
            print('error')
    elif 'size' in cmd:
        print(len(stack))
    elif 'clear' in cmd:
        stack.clear()
        print('ok')
    cmd = input()
print('bye')

