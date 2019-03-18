def binary_search(arr, val, left, right):
	n = len(arr)
	mid = (left + right) // 2

	if left == right:
		if arr[left] == val:
			return left
		else:
			return None

	if arr[mid] == val:
		return mid
	elif arr[mid] < val:
		return binary_search(arr, val, mid+1, right)
	elif arr[n//2] > val:
		return binary_search(arr, val, left, mid-1)

print(binary_search(list(range(10)), 9, 0, 9) == 9)
print(binary_search(list(range(10)), 10, 0, 9) == None)