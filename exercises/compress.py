def compress(s):
	n = len(s)
	s_comp = s[0]
	count = 1

	for i in range(1,n):
		c = s[i]

		if c == s[i-1]:
			count += 1
		else:
			s_comp += str(count) + c
			count = 1

		if i == n-1:
			s_comp += str(count)

	if len(s_comp) < n:
		return s_comp
	else:
		return s

s = 'aabcccccaaa'
print(compress(s) == 'a2b1c5a3')