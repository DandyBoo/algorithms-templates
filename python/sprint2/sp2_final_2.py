# 81277540
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


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
        if data in '+-*/':
            op2 = stack.pop()
            op1 = stack.pop()
            res = OPERATORS[data]
            stack.push(res(op1, op2))
        else:
            stack.push(int(data))
    print(stack.pop())
