def bin_search(var_list, var):
    if var == 0 and var not in var_list:
        return None
    n = len(var_list)
    l = -1
    r = n
    while r - l > 1:
        m = int((l + r) / 2)
        if var_list[m] < var:
            l = m
        else:
            r = m
    if var_list[r] == var:
        return r
    else:
        return None
