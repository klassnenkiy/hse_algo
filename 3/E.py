n = int(input())
ln= list(map(int, input().split()))
m = int(input())
lm= list(map(int, input().split()))

def merge(l1,l2):
    l = []
    i,j=0,0
    while i<n and j <m:
        if l1[i]<=l2[j]:
            l.append(l1[i])
            i+=1
        else:
            l.append(l2[j])
            j += 1
    l += l1[i:]+l2[j:]
    return l

print(*merge(ln,lm))