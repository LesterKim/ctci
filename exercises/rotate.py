def swap(a, b):
	c = a
	a = b
	b = c

	return (a,b)

def rotate(M):
	n = len(M)

	if n == 1:
		return M

	for j in range(n//2):
		for i in range(j, n-1-j):
			(M[j][i], M[i][n-1-j]) = swap(M[j][i], M[i][n-1-j])

		for i in range(j, n-1-j):
			(M[i][n-1-j], M[n-1-j][n-1-i]) = swap(M[i][n-1-j], M[n-1-j][n-1-i])

		for i in range(j, n-1-j):
			(M[n-1-j][n-1-i], M[n-1-i][j]) = swap(M[n-1-j][n-1-i], M[n-1-i][j])

	return M

n = 5
M = [list(range(n*i, n*(i+1))) for i in range(n)]

for r in rotate(M):
	print(r)