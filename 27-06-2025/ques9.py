lst = [1, 2, 2, 3, 4, 4, 5]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print(unique)
