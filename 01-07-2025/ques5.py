def count_cases(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    digit = sum(1 for c in s if c.isdigit())
    return upper, lower, digit
print(count_cases("Hello123")) 
