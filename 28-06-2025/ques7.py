//Print all distinct values in a list of dictionaries
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
unique_values = {value for d in data for value in d.values()}
print("Unique Values:", unique_values)
