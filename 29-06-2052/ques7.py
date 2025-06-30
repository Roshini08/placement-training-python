from collections import Counter

def merge_dicts_add_values(d1, d2):
    return dict(Counter(d1) + Counter(d2))
d1 = {'a': 2, 'b': 3}
d2 = {'a': 1, 'c': 4}
print(merge_dicts_add_values(d1, d2))  
