# def find_day_binary(arr, price, left, right):
#     if right <= left:
#         return -1
#     mid = (left - right) // 2
#     if price <= arr[mid] != arr[mid - 1]:
#         return mid + 1
#     else:
#
#     if arr[mid] >= price:
#
#     pass

# 1 2 3 4 4 4 4 5 5 5
def find_day_binary(arr, price, left, right):
    if right <= left:
        return -1
    middle = (left + right) // 2
    if arr[middle] >= price and (arr[middle - 1] < price or middle == 0):
        return middle + 1
    elif price <= arr[middle]:
        return find_day_binary(arr, price, left, middle)
    else:
        return find_day_binary(arr, price, middle + 1, right)


days = int(input())
arr = [int(num) for num in input().split(' ')]
price = int(input())
print(find_day_binary(arr, price, left=0, right=days), end=' ')
print(find_day_binary(arr, price * 2, left=0, right=days))
