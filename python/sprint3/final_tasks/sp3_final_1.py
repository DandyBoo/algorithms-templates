# 81912899
def broken_search(nums, target) -> int:
    start_index = 0
    end_index = len(nums) - 1
    while start_index <= end_index:
        middle = (start_index + end_index) // 2
        if nums[middle] == target:
            return middle
        elif nums[start_index] <= nums[middle]:
            if nums[start_index] <= target < nums[middle]:
                end_index = middle - 1
            else:
                start_index = middle + 1
        else:
            if nums[middle] < target <= nums[end_index]:
                start_index = middle + 1
            else:
                end_index = middle - 1

    return -1


if __name__ == '__main__':
    _ = input()
    target = int(input())
    nums = list(map(int, input().split()))
    print(broken_search(nums, target))
