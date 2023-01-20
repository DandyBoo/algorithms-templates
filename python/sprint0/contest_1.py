j = input()
s = input()
res = 0
for item in s:
    if item in j:
        res += 1
print(res)

# import sys
#
# j = sys.stdin.readline().strip()
# s = sys.stdin.readline().strip()
#
# result = 0
# for ch in s:
#     if ch in j:
#         result += 1
#
# print(result)
# print(j)
# print(s)
