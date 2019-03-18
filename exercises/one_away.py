def one_away(s1, s2):
	s1_alph_counts = [0]*26
	s2_alph_counts = [0]*26

	for c in s1:
		s1_alph_counts[ord(c)-97] += 1

	for c in s2:
		s2_alph_counts[ord(c)-97] += 1

	s1_s2_diff = [i - j for i, j in zip(s1_alph_counts, s2_alph_counts)]

	final = list(filter(lambda x: x != 0, s1_s2_diff))
	fin_sum = sum(final)

	if len(final) <= 2:
		if fin_sum == 0:
			return True
		else:
			return abs(fin_sum) == 1

	return False

a = 'pale'
b = 'ple'

c = 'pale'
d = 'pales'

e = 'pale'
f = 'bale'

g = 'pale'
h = 'bake'

print(one_away(a,b))
print(one_away(c,d))
print(one_away(e,f))
print(one_away(g,h))