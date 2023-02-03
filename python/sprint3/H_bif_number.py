def big_number(num, arr):
    for i in range(num - 1):
        for j in range(0, num - i - 1):
            var1 = arr[j] + arr[j + 1]
            var2 = arr[j + 1] + arr[j]
            if var1 < var2:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("".join(arr))


if __name__ == '__main__':
    num = int(input())
    arr = input().split(' ')
    big_number(num, arr)
