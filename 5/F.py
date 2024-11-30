n = int(input())
arr = [input() for i in range(n)]

print('Initial array:')
print(', '.join(arr))
print('*'*10)
for i in range(1,len(arr[0])+1):
    print(f'Phase {i}')
    res = []
    for j in range(0, 10):
        s = []
        for number in arr:
            if number[-i] == str(j):
                s.append(number)
        if s != []: res += s
        if s == []:
            s = ['empty']
        print(f'Bucket {j}: ' + ', '.join(s))
    arr = res
    print('*'*10)
print('Sorted array:')
print(', '.join(arr))
