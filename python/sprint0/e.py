from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    # left = 0
    # right = len(arr) - 1
    # while left < right:
    #     if arr[left] + arr[right] == target_sum:
    #         return arr[left], arr[right]
    #     if arr[left] + arr[right] < target_sum:
    #         left += 1
    #     else:
    #         right -= 1
    # return None
    previous = set()
    for i in range(len(arr)):
        x = target_sum - arr[i]
        if x in previous:
            return arr[i], x
        previous.add(arr[i])
    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
