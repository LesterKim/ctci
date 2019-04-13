def count_islands(M):
	count = 0

	m = len(M)
	n = len(M[0])

	visited = [ [False for i in range(n)] for i in range(m) ]

	def dfs(M, i, j, visited):
		#print(i,j)
		
		if M[i][j] == 1 and not visited[i][j]:
			visited[i][j] = True

		min_k = max(i-1, 0)
		min_l = max(j-1, 0)

		max_k = min(i+1, m)
		max_l = min(j+1, n)

		for k in range(min_k, max_k):
			for l in range(min_l, max_l):
				if M[k][l] == 1 and not visited[k][l]:
					dfs(M, k, l, visited)

	for i in range(m):
		for j in range(n):
			if M[i][j] == 1 and not visited[i][j]:
				dfs(M, i, j, visited)
				count += 1

	return count

M = [[1, 1, 0, 0, 0], \
	 [0, 1, 0, 0, 1], \
	 [1, 0, 0, 1, 1], \
	 [0, 0, 0, 0, 0], \
	 [1, 0, 1, 0, 1]]

print(count_islands(M))# == 3)