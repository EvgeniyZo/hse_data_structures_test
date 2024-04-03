
def sort(a):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                tmp = a[i]
                a[i] = a[i-1]
                a[i-1] = tmp
                sorted = False
    return a
    
