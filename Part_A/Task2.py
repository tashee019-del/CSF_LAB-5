def is_balanced(expr):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expr:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return "Not Balanced"
    return "Balanced" if not stack else "Not Balanced"

print(is_balanced("(a+b)*(c+d)"))
