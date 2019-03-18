def is_pal_perm(s):
	alph_counts = [0]*26

	for c in s:
		alph_counts[ord(c) - 97] += 1

	c_odds = list(filter(lambda x: x % 2 == 1, alph_counts))

	return len(c_odds) < 2

s = 'oactcat'
print(is_pal_perm(s))

s = 'zacocat'
print(is_pal_perm(s))

s = 'aabbbcccaa'
print(is_pal_perm(s))