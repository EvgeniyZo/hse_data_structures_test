
def sort(arr):
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be numbers.")
    return sorted(arr)
