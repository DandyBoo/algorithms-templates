def bubble_sort(num, arr):
    flag = 1
    for i in range(num - 1):
        for j in range(0, num - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 1:
            print(' '.join(arr))
            flag = 0
        else:
            break


if __name__ == '__main__':
    num = int(input())
    arr = input().split(' ')
    bubble_sort(num, arr)
