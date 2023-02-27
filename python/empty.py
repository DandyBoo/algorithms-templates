# def gen_binary(n, prefix):
#     if n == 0:
#         # print(prefix)
#         yield prefix
#         return
#     else:
#         yield from gen_binary(n - 1, prefix + '0')
#         yield from gen_binary(n - 1, prefix + '1')
#
#
# for i in gen_binary(2, ''):
#     print(i)


# def bracket_generator(control, left, right, prefix):
#     if left == 0 and right == 0:
#         # print(prefix)
#         yield prefix
#
#     else:
#         if left > 0:
#             yield from bracket_generator(control + 1, left - 1, right, prefix + '(')
#
#         if control > 0 and right > 0:
#             yield from bracket_generator(control - 1, left, right - 1, prefix + ')')
#
#
# n = left = right = int(input())
# control = 0
# for i in bracket_generator(control, left, right, ''):
#     print(i)

# def broken_search(nums: list, target: int) -> int:
#     start_idx = 0
#     end_idx = len(nums) - 1
#     while start_idx <= end_idx:
#         mid_idx = (start_idx + end_idx) // 2
#         if nums[mid_idx] == target:
#             return mid_idx
#         elif nums[start_idx] <= nums[mid_idx]:
#             if nums[start_idx] <= target < nums[mid_idx]:
#                 end_idx = mid_idx - 1
#             else:
#                 start_idx = mid_idx + 1
#         else:
#             if nums[mid_idx] < target <= nums[end_idx]:
#                 start_idx = mid_idx + 1
#             else:
#                 end_idx = mid_idx - 1
#     return -1
#
#
# if __name__ == '__main__':
#     count_array = int(input())
#     target_number = int(input())
#     numbers_array = [int(num) for num in input().split()]
#
#     print(broken_search(numbers_array, target_number))

