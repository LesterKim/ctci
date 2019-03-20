def cont_seq(arr):
  n = len(arr)
  i = 0
  maxi = max(arr)
  summ = 0
  interval = [0, 0]

  while i < n:
    for j in range(i, n):
      summ += arr[j]

      if summ < 0:
        summ = 0
        i = j+1
        break

      if summ >= maxi:
        maxi = summ
        interval = [i, j]

      if j == n-1:
        i = n

  return interval


arr = [2, -8, 3, -2, 4, -10]
arr2 = [2, 3, -8, -1, 2, 4, -2, 3]

print(cont_seq(arr))
print(cont_seq(arr2))
