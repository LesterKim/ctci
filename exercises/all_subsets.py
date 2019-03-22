# [1, 2] -> [[], [1], [2], [1,2]]

def all_subsets(arr):
	n = len(arr)

	if n == 0:
		return [arr]
	else:
		small_subsets = all_subsets(arr[:n-1])
		m = len(small_subsets)
		subsets = small_subsets

		for i in range(m):
			subsets.append(subsets[i] + [arr[n-1]])

		return subsets

n = 3
arr = list(range(n))
print(all_subsets(arr))