from random import randint

def quicksort(arr):
	if len(arr) > 1:
		[arr, q] = random_partition(arr)
		return quicksort(arr[:q]) + [arr[q]] + quicksort(arr[q+1:])
	else:
		return arr

def partition(arr):
	n = len(arr)
	x = arr[n-1]
	i = -1

	for j in range(n-1):
		if arr[j] <= x:
			i += 1
			arr = exchange(arr, i, j)

	arr = exchange(arr, i+1, n-1)

	return [arr, i+1]

def random_partition(arr):
	n = len(arr)
	i = randint(0,n-1)
	arr = exchange(arr, i, n-1)

	return partition(arr)

def exchange(arr, i, j):
	dum = arr[i]
	arr[i] = arr[j]
	arr[j] = dum

	return arr

ary = [4, 2, 9, 6, 1, 0]
ary2 = [5, 1, 3, 6, 9, 8, 7]

print(quicksort(ary) == sorted(ary))
print(quicksort(ary2) == sorted(ary2))