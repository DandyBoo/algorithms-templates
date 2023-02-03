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


def bracket_generator(control, left, right, prefix):
    if left == 0 and right == 0:
        # print(prefix)
        yield prefix

    else:
        if left > 0:
            yield from bracket_generator(control + 1, left - 1, right, prefix + '(')

        if control > 0 and right > 0:
            yield from bracket_generator(control - 1, left, right - 1, prefix + ')')


n = left = right = int(input())
control = 0
for i in bracket_generator(control, left, right, ''):
    print(i)
