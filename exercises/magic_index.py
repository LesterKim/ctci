def magic_index(arr, a, b):
	if a > b:
		return -1
	elif a == b:
		return a if arr[a] == a else -1

	m = (a+b) // 2

	if arr[m] == m:
		return m

	left = magic_index(arr, a, min(m-1, arr[m]))

	if left > -1:
		return left

	right = magic_index(arr, max(m+1, arr[m]), b)

	return right

a = list(range(5))
b = [-10, -1, 0, 3, 5, 6]
c = [-2, -2, 0, 0, 0, 0, 1, 2, 3, 4, 6, 14, 14, 14, 14]
d = [100]*50

print(magic_index(a, 0, len(a)-1))
print(magic_index(b, 0, len(b)-1))
print(magic_index(c, 0, len(c)-1))
print(magic_index(d, 0, len(d)-1))