def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))
print(sort_dict_by_values({'a': 3, 'b': 1, 'c': 2}))

