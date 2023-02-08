def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def mergesort(L):
    if len(L) < 2:
        return L
    middle = len(L) // 2
    left = mergesort(L[:middle])
    right = mergesort(L[middle:])
    out = merge(left, right)
    return out


print(mergesort([5, 4, 3, 2, 1]))
