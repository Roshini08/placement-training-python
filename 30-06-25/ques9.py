from collections import OrderedDict

def first_unique_char(s):
    count = OrderedDict()
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch, freq in count.items():
        if freq == 1:
            return ch
    return None

print(first_unique_char("swiss")) 
