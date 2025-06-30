def find_pairs(lst, target):
    seen = set()
    pairs = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)

# Example
print(find_pairs([1, 3, 2, 2, 4, 0, 5], 4))  
