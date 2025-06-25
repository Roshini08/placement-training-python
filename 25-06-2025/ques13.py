n = int(input("Enter number: "))
if n < 2:
    print("Not Prime")
elif all(n % i != 0 for i in range(2, int(n**0.5)+1)):
    print("Prime")
else:
    print("Not Prime")
