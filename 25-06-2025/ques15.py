a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+ - * /): ")

if op == '+': print(a + b)
elif op == '-': print(a - b)
elif op == '*': print(a * b)
elif op == '/': print(a / b if b != 0 else "Division by zero!")
else: print("Invalid operator")
