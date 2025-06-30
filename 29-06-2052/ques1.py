from collections import Counter

def second_most_frequent(s):
    freq = Counter(s)
    most_common = freq.most_common()
    return most_common[1][0] if len(most_common) > 1 else None

# Example
print(second_most_frequent("successes"))  
