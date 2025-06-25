def primes_in_range(start, end):
    for num in range(start, end+1):
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)) and num > 1:
            print(num, end=' ')

primes_in_range(10, 50)
