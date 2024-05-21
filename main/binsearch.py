
def binsearchl(arr, num):
    l = 0
    r = len(arr) - 1
    while (l < r):
        pivot = (r + l) // 2
        if (arr[pivot] < num):
            l = pivot + 1
        else:
            r = pivot            
    return r


def binsearchr(arr, num):
    l = 0
    r = len(arr) - 1
    while (l < r):
        pivot = (r + l) // 2
        if (arr[pivot] > num):
            r = pivot
        else:
            l = pivot + 1
    return l - 1