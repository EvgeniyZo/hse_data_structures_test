
def sort(a):
    N = len(a)
    i = 0
    while i < N - 1:
        j = 0
        while j < N - 1 - i:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
        i += 1
    return a
