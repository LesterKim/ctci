def zero_matrix(M):
	m = len(M)
	n = len(M[0])

	arr = []

	for i in range(m):
		for j in range(n):
			if M[i][j] == 0:
				arr.append([i,j])

	rows = list(set([p[0] for p in arr]))
	cols = list(set([p[1] for p in arr]))

	for r in rows:
		M[r] = [0]*n

	for i in range(m):
		for c in cols:
			M[i][c] = 0

	return M

M = [[1,1,1,1,1], [1,0,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,0,1]]

for r in M:
	print(r)

print('\n')

for r in zero_matrix(M):
	print(r)