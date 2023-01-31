# from typing import List
#
#
# def generateParenthesis(n: int) -> List[str]:
#
#     def helper(ans, s, left, right):
#         if left == 0 and right == 0:
#             ans.append(s)
#
#         if left > 0:
#             helper(ans, s + '(', left - 1, right)
#
#         if right > 0 and left < right:
#             helper(ans, s + ')', left, right - 1)
#
#     ans = []
#     helper(ans, '', n, n)
#
#     return ans
#
#
# n = int(input())
# for i in generateParenthesis(n):
#     print(i)

# 2nd way
def generate_parenthesis(control, left, right, prefix):
    if left == 0 and right == 0:
        print(prefix)
    else:
        if left > 0:
            generate_parenthesis(control + 1, left - 1, right, prefix + '(')
        if control > 0 and right > 0:
            generate_parenthesis(control - 1, left, right - 1, prefix + ')')


n = left = right = int(input())
control = 0
generate_parenthesis(control, left, right, '')
