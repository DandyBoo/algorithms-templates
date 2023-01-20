class MaxEffective:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        if len(self.items) == 0:
            self.max.append(int(item))
        elif int(item) > self.max[len(self.items) - 1]:
            self.max.append(int(item))
        else:
            self.max.append(self.max[len(self.items) - 1])
        self.items.append(item)

    def pop(self):
        if not self.items:
            return "error"
        self.max.pop()
        return self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            return None
        return self.max[len(self.items) - 1]


def main():
    stack = MaxEffective()
    n = int(input())
    res = []
    for _ in range(n):
        instruction = input().split()
        if instruction[0] == "push":
            stack.push(int(instruction[1]))
        elif instruction[0] == "pop":
            if stack.pop() == "error":
                res.append("error")
        elif instruction[0] == "get_max":
            if stack.get_max() == "None":
                res.append("None")
            else:
                res.append(stack.get_max())
    for i in res:
        print(i)


if __name__ == '__main__':
    main()
