l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

card = 0
while l1 and l2:
    card += 1
    first = l1.pop(0)
    second = l2.pop(0)
    if (first > second and not (first == 9 and second == 0)) or (first == 0 and second == 9):
        l1 += [first, second]
    else:
        l2 += [first, second]
    if card == 10**6:
        print('botva')
        break
else:
    if l2:
        print('second',card)
    else:
        print('first',card)
