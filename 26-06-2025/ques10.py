def find_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        if target - num in seen:
            pairs.add((min(num, target - num), max(num, target - num)))
        seen.add(num)
    return list(pairs)
