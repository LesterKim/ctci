def merge_sort(arr):
	n = len(arr)

	if n < 2:
		return arr
	else:
		return merge(merge_sort(arr[:n//2]), merge_sort(arr[n//2:]))

def merge(arr, brr):
	merged = []

	m = len(arr)
	n = len(brr)

	i = 0
	j = 0

	while i < m or j < n:
		if arr[i] < brr[j]:
			merged.append(arr[i])
			i += 1
		else:
			merged.append(brr[j])
			j += 1

		if i == m:
			return merged + brr[j:]
		if j == n:
			return merged + arr[i:]

#print(merge([1,3,9], [0,2,7]))

print(merge_sort([4, 2, 9, 6, 1, 0]))