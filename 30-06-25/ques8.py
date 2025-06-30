from collections import Counter

def find_repeats(lst):
    return [k for k, v in Counter(lst).items() if v > 1]

print(find_repeats([1,2,3,2,1,4])) 
