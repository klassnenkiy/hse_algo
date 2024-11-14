stack = []
cmd = input()

while cmd != 'exit':
    if 'push' in cmd:
        pussh, n = cmd.split()
        stack.append(n)
        print('ok')
    elif 'pop' in cmd:
        print(stack.pop())
    elif 'back' in cmd:
        print(stack[-1])
    elif 'size' in cmd:
        print(len(stack))
    elif 'clear' in cmd:
        stack.clear()
        print('ok')
    cmd = input()
print('bye')

