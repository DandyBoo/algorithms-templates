from typing import List


def sorted_sq(nums: List) -> List:
    left = 0
    right = i = len(nums) - 1
    res = [None] * len(nums)
    while left <= right:
        if nums[left] ** 2 > nums[right] ** 2:
            res[i] = nums[left] ** 2
            left += 1
        else:
            res[i] = nums[right] ** 2
            right -= 1
        i -= 1
    return res


nums = [-6, -3, -2, -1, 0, 3, 5, 6, 7]
print(sorted_sq(nums))
