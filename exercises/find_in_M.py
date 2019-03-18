def find_in_M(M, val, a, b, c, d):
	if a == b and c == d:
		if M[a][c] != val: return None

	if a > b or c > d: return None

	m = (a+b)//2
	n = (c+d)//2

	if M[m][n] == val:
		return [m, n]
	elif M[m][n] < val:
		below = find_in_M(M, val, m+1, b, c, d)

		if below != None:
			return below

		return find_in_M(M, val, a, m, n+1, d)
	else:
		above = find_in_M(M, val, a, m-1, c, d)

		if above != None:
			return above

		return find_in_M(M, val, m, b, c, n-1)

n = 5
M = [list(range(n*i, n*(i+1))) for i in range(n)]

for r in M:
	print(r)

print('\n')

print(find_in_M(M, 30, 0, n-1, 0, n-1))
print(find_in_M(M, 6, 0, n-1, 0, n-1))
print(find_in_M(M, 18, 0, n-1, 0, n-1))