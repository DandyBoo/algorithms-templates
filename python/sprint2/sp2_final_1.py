# 81239413
class DequeException(Exception):
    pass


class CircularDeque:
    def __init__(self, size: int):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.size == self.head

    def push_front(self, item):
        if self.is_full():
            raise DequeException("Deque is full")
        if self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.head = (self.head - 1 + self.size) % self.size
        self.queue[self.head] = item

    def push_back(self, item):
        if self.is_full():
            raise DequeException("Deque is full")
        if self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = item

    def pop_front(self):
        if self.is_empty():
            raise DequeException("Deque is empty")
        item = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return item

    def pop_back(self):
        if self.is_empty():
            raise DequeException("Deque is empty")
        item = self.queue[self.tail]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.tail = (self.tail - 1 + self.size) % self.size
        return item


def main():
    number_of_instructions = int(input())
    max_size = int(input())
    deque = CircularDeque(max_size)
    result = []
    INSTRUCTIONS_WITH_PARAMS = ("push_back", "push_front")
    for _ in range(number_of_instructions):
        instruction = input().split()
        method = getattr(deque, instruction[0])
        if instruction[0] in INSTRUCTIONS_WITH_PARAMS:
            try:
                method(instruction[1])
            except DequeException:
                result.append("error")
        else:
            try:
                result.append(method())
            except DequeException:
                result.append("error")

    for res in result:
        print(res)


if __name__ == '__main__':
    main()
