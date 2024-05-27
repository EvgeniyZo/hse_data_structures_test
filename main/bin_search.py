def bin_search(var_list, var):
    n = len(var_list)
    l = -1
    r = n
    while r - l > 1:
        m = int((l + r) / 2)
        if var_list[m] < var:
            l = m
        else:
            r = m
    return r
