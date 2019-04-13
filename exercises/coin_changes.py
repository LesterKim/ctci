# 10 -> 1*10 , 2*5 , 10*1 , 1*5 + 5*1
denoms = [100, 50, 25, 10, 5, 1]

def make_change(n, denoms):
	first_denom = denoms[0]

	if first_denom == 1:
		return 1

	q = n // first_denom
	count = 0

	for i in range(q+1):
		count += make_change(n - i*first_denom, denoms[1:])

	return count

print(make_change(100, denoms))