# 82018687
from dataclasses import dataclass


@dataclass
class Participant:
    # Эксперимент по снижению используемой памяти:
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


def quicksort(arr, low, high):
    if low >= high:
        return

    left, right = low, high
    pivot = arr[(low + high) // 2]

    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    quicksort(arr, low=low, high=right)
    quicksort(arr, low=left, high=high)


if __name__ == '__main__':
    n = int(input())
    results = []

    for _ in range(n):
        name, solved, penalty = input().split()
        results.append(Participant(name, int(solved), int(penalty)))

    quicksort(results, low=0, high=n-1)

    print(*results, sep='\n')
