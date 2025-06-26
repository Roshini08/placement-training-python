def lis(arr):
    from bisect import bisect_left
    sub = []
    for x in arr:
        i = bisect_left(sub, x)
        if i == len(sub):
            sub.append(x)
        else:
            sub[i] = x
    return len(sub)
