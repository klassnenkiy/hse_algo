n = int(input())
l= list(map(int, input().split()))

for i in range(1,n):
    p = l[i]
    j = i-1
    c=0
    while j>=0 and l[j] > p:
        l[j+1]=l[j]
        j -=1
        c+=1
    l[j+1] = p
    if c !=0:
        print(*l)