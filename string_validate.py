# check if a string containing parenthesis() ,brackets[] ,braces{} is valid

def isValid(s):

    stack = []

    for ch in s:
        if ch == '{' or ch == '[' or ch == '(' :
            stack.append(ch)

        elif ch == '}':
            if not stack or stack[-1] != '{':
                return False
            stack.pop()
        
        elif ch == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
        
        elif ch == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return len(stack) == 0


print(isValid("{([])}"))
print(isValid("{(])}"))
print(isValid("([])}"))
print(isValid("()"))
print(isValid("{"))
print(isValid(""))
