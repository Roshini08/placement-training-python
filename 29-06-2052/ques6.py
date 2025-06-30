def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)

# Example
print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))  
