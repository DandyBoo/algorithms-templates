def merge(arr, lf, mid, rg):
	result = []
	a = arr[lf:mid]
	b = arr[mid:rg]
	i, j = 0, 0
	while i < len(a) and j < len(b):
		if a[i] <= b[j]:
			result.append(a[i])
			i += 1
		else:
			result.append(b[j])
			j += 1
	result += a[i:] + b[j:]
	# result += b[j:]
	return result


def merge_sort(arr, lf, rg):
	if len(arr[lf:rg]) >= 2:
		mid = (rg + lf) // 2
		merge_sort(arr, lf, mid)
		merge_sort(arr, mid, rg)
		arr[lf:rg] = merge(arr, lf, mid, rg)


def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0, 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected


if __name__ == '__main__':
	test()
