def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def pascal(n):
    for i in range(n):
        for j in range(n - i + 1):
            print(" ", end="")
        for j in range(i + 1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print()

rows = int(input("Enter number of rows: "))
pascal(rows)
