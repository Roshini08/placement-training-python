def common_three_lists(a, b, c):
    return list(set(a) & set(b) & set(c))
print(common_three_lists([1,2,3], [2,3,4], [3,2,5]))  
