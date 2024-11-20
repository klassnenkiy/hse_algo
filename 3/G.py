n=int(input())
l=list(map(int, input().split()))

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

def split(l):
    s = len(l) // 2
    l1 = l[:s]
    l2 = l[s:]
    if len(l1) > 1:
        l1 = split(l1)
    if len(l2) > 1:
        l2 = split(l2)
    return merge(l1, l2)

print(*split(l))