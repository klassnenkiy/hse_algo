cmd = input()
stack = []
flag = True
for i in cmd:
    if i in '([{':
        stack.append(i)
    elif i in ')]}':
        if len(stack) != 0:
            a = stack.pop()
            if (a == '(' and i == ')') or (a == '{' and i == '}') or (a == '[' and i == ']'):
                continue
            else:
                flag = False
                break
        else:
            flag = False
            break
if flag and len(stack) == 0:
    print('yes')
else:
    print('no')
