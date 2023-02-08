from dataclasses import dataclass


@dataclass
class Participant:
    # Эксперимент по снижению потребляемой памяти:
    __slots__ = ['name', 'solved', 'penalty']
    name: str
    solved: int
    penalty: int

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return (
                (-self.solved, self.penalty, self.name)
                < (-other.solved, other.penalty, other.name)
        )


def quicksort(array, low, high):

    def _quicksort(low, high):
        if low >= high:
            return
        left = low
        right = high
        pivot = array[(right + left) // 2]
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort(low, right)
        _quicksort(left, high)

    _quicksort(low, high - 1)


if __name__ == '__main__':
    n = int(input())
    results = []

    for _ in range(n):
        name, solved, penalty = input().split()
        results.append(Participant(name, int(solved), int(penalty)))

    quicksort(results, low=0, high=n)

    print(*results, sep='\n')
