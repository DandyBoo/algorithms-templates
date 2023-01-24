# 81295457
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError("Error: stack is empty")


if __name__ == '__main__':
    expression = input().split()
    stack = Stack()
    OPERATORS = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b
    }
    for data in expression:
        if data in OPERATORS.keys():
            op2 = stack.pop()
            op1 = stack.pop()
            res = OPERATORS[data]
            stack.push(res(op1, op2))
        else:
            stack.push(int(data))
    print(stack.pop())
