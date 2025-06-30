def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

print(digital_root(9875))
