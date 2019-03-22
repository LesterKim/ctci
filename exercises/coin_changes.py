# 10 -> 1*10 , 2*5 , 10*1 , 1*5 + 5*1
denoms = [100, 50, 25, 10, 5, 1]

def make_change(n, denoms):
	count = 0

	for denom in denoms:
		while n >= denom:
			n -= denom
			count += make_change(n, denoms)
"""
def coin_changes(n):
	if n >= 25:
		q = n // 25

		for i in range(q+1):
			total += 

		return 

		n -= 25*q

	elif n >= 10:


	while n >= 25:
		n /

	if n < 5:
		return 1
	elif n < 10:
		return coin_changes(n-5) + 1
	elif n < 25:
		return coin_changes(n-10) + 3
	else:
		return coin_changes(n-25) + 12
"""
#print(coin_changes(98))



# 5 -> 1*5, 5*1
# 10 -> 1*10, 2*5, 1*5 + 5*1, 10*1

""" 25 -> 1*25,
	2*10 + 1*5, 2*10 + 5*1,
	1*10 + 3*5, 1*10 + 2*5 + 5*1, 1*10 + 1*5 + 10*1, 1*10 + 15*1,
	5*5, 4*5 + 5*1, 3*5 + 10*1, 2*5 + 15*1, 1*5 + 20*1, 25*1
"""

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