class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) <= 0:
            return "Stack Empty"
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)


def check_parentheses(input):
    if len(input) % 2 != 0:
        return False

    open_paren = ["(", "{", "["]
    clos_paren = [")", "}", "]"]

    s = Stack()

    for c in input:
        if c in clos_paren:
            if s.size() == 0:
                return False
            else:
                popped_ch = s.pop()
                if clos_paren.index(c) != open_paren.index(popped_ch):
                    return False
        else:
            s.push(c)

    if s.size() == 0:
        return True
    else:
        return False


print check_parentheses("{({(})}")
