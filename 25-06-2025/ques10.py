def is_balanced(expr):
    stack = []
    for char in expr:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or {')':'(', ']':'[', '}':'{'}.get(char) != stack.pop():
                return False
    return not stack

print(is_balanced("({[]})"))  # True
