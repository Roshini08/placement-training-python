def find_missing(lst, n):
    return n * (n + 1) // 2 - sum(lst)

print(find_missing([1, 2, 4, 5], 5))  
