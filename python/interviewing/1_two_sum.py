from typing import List


def two_sum(arr: List, target: int) -> List:
    seen = {}
    for i, v in enumerate(arr):
        num = target - v
        if num in seen:
            return [i, seen[num]]
        seen[v] = i


arr = [1, 2, 5, 7, 9]
print(two_sum(arr, 7))
