s = input("Enter a string: ").lower().replace(" ", "")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
