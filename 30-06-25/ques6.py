def remove_consecutive_duplicates(lst):
    result = [lst[0]] if lst else []
    for item in lst[1:]:
        if item != result[-1]:
            result.append(item)
    return result
print(remove_consecutive_duplicates([1,1,2,2,3,1,1]))  
