"""
Дан массив целых чисел от 1 до N (1, 2, 3, ... N).
Из него два числа удалили, оставшийся массив перемешали.
Необходимо эти найти два числа.
"""
from typing import List


def find_sum_of_two(arr: List) -> int:
    r_len = len(arr) + 2
    return int(r_len * (r_len + 1) / 2 - sum(arr))


def find_two_deleted(arr: List) -> List:
    s_arr = sorted(arr)
    for ind, val in enumerate(s_arr):
        if (ind + 1) != val:
            return [ind + 1, find_sum_of_two(arr) - (ind + 1)]
    return [len(arr) + 1, len(arr) + 2]


print(find_two_deleted([1, 2, 3, 4, 5, 6, 7, 8]))
print(find_two_deleted([3, 4, 5, 6, 7, 8]))
print(find_two_deleted([1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13]))
print(find_two_deleted([1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14]))
