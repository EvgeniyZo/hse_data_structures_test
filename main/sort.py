
def sort(a):
    if (len(a) == 1):
        return a    
    l1, l2 = divide(a)
    l1 = sort(l1)
    l2 = sort(l2)
    l = merge(l1, l2)
    return l

def divide(a):
    pivot = len(a) // 2
    l1 = a[:pivot]
    l2 = a[pivot:]
    return l1, l2

def merge(l1, l2):
    i1 = 0
    i2 = 0
    l = list()    
    if (len(l1) > len(l2)):
        l1, l2 = l2, l1
    while (i1 < len(l1) and i2 < len(l2)):
        if (l1[i1] < l2[i2]):
            l.append(l1[i1])
            i1 += 1
        else:
            l.append(l2[i2])
            i2 += 1
    while (i1 < len(l1)):
        l.append(l1[i1])
        i1 += 1
    while (i2 < len(l2)):
        l.append(l2[i2])
        i2 += 1

    return l