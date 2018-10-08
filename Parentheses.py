def parentheses_check(s):
    stack = []
    open_braces = ["{", "[", "("]
    close_braces = ["}", "]", ")"]

    for c in s:
        if c in open_braces:
            stack.append(c)
        elif c in close_braces:
            if len(stack) == 0:
                return False
            match = stack.pop()
            if open_braces.index(match) == close_braces.index(c):
                pass
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


print parentheses_check("{}(()))[][]")