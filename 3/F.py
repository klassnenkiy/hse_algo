n,m,k = map(int, input().split())
l1=list(map(int, input().split()))
l2=list(map(int, input().split()))
l3=list(map(int, input().split()))

def merge(l1,l2):
    l = []
    i,j=0,0
    while i<len(l1) and j <len(l2):
        if l1[i]<=l2[j]:
            l.append(l1[i])
            i+=1
        else:
            l.append(l2[j])
            j += 1
    l += l1[i:]+l2[j:]
    return l

print(*merge(merge(l1,l2),l3))
