# 81065808	
class CircularDeque:
    def __init__(self, m: int):
        self.m = m
        self.queue = [None] * m
        self.head = self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.m == self.head

    def push_front(self, item):
        if self.is_full():
            return "error"
        if self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.head = (self.head - 1 + self.m) % self.m
        self.queue[self.head] = item

    def push_back(self, item):
        if self.is_full():
            return "error"
        if self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.m
        self.queue[self.tail] = item

    def pop_front(self):
        if self.is_empty():
            return "error"
        item = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.m
        return item

    def pop_back(self):
        if self.is_empty():
            return "error"
        item = self.queue[self.tail]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.tail = (self.tail - 1 + self.m) % self.m
        return item


def main():
    n = int(input())
    m = int(input())
    deque = CircularDeque(m)
    result = []
    for _ in range(n):
        instruction = input().split()
        if instruction[0] == "push_back":
            if deque.push_back(int(instruction[1])) == "error":
                result.append("error")
        if instruction[0] == "push_front":
            if deque.push_front(int(instruction[1])) == "error":
                result.append("error")
        if instruction[0] == "pop_back":
            result.append(deque.pop_back())
        if instruction[0] == "pop_front":
            result.append(deque.pop_front())

    for i in result:
        print(i)


if __name__ == '__main__':
    main()
