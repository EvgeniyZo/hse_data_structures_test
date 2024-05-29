def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


def sort(a):
    return quicksort(a)


# if __name__ == "__main__":
#     arr = [5, 1, 7, 8, 5, 3, 4, 2]
#     print(sorted(arr))
#     print(sort(arr))
