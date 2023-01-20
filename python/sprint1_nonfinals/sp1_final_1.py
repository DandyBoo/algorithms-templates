# 80531193
def nearest_zero(street_len, numbers):
    res = street_len * [0]
    for i in range(street_len):
        if numbers[i] == 0:
            first_zero = i
            break
    count = 1
    for i in range(first_zero, street_len):
        if numbers[i] == 0:
            count = 1
        else:
            res[i] = count
            count += 1

    rev_order = numbers[::-1]
    rev_res = res[::-1]

    for i in range(street_len - first_zero):
        if rev_order[i] == 0:
            count = 1

        else:
            rev_res[i] = min(count, rev_res[i])
            count += 1

    for i in range(street_len - first_zero, street_len):
        rev_res[i] = count
        count += 1

    return rev_res[::-1]


def main():
    street_len = int(input())
    numbers = list(map(int, input().split()))
    print(*nearest_zero(street_len, numbers))


if __name__ == '__main__':
    main()
