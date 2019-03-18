from math import ceil, sqrt

def sieve(n):
	primes = [2]

	array = list(range(3,n+1,2))

	while len(array) > 0:
		div = array.pop(0)
		primes.append(div)

		array = list(filter(lambda x: x % div != 0, array))

	return primes

def primality(n):
	n_sqrt = ceil(sqrt(n))

	primes = sieve(n_sqrt)

	for i in primes:
		if n % i == 0:
			return True

	return False

n = 2**32-1
print(n)
print(len(sieve(ceil(sqrt(n)))))
print(primality(n))