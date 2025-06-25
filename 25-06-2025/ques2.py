import math
num = int(input("Enter number: "))
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += math.factorial(digit)
    temp //= 10
print("Strong number" if total == num else "Not a strong number")
