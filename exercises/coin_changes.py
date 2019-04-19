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

def make_change2(n, denoms):
	if n < 5: return 1

	if len(denoms) == 1: return 1

	for i, denom in enumerate(denoms):
		if n >= denom:
			return make_change2(n-denom, denoms) + make_change2(n, denoms[i+1:])

assert make_change(100, denoms) == 293
assert make_change2(100, denoms) == 293