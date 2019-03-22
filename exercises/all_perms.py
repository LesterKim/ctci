def all_perms(s):
	n = len(s)

	if n < 2:
		return [s]
	else:
		sub_perms = all_perms(s[:n-1])
		perms = []

		for perm in sub_perms:
			list_perm = list(perm)

			for i in range(n):
				c_n = s[n-1]

				if i < n-1:
					temp = perm[i]
					list_perm[i] = c_n
					new_perm = list_perm + [temp]
					list_perm[i] = temp
					perms.append(''.join(new_perm))
				else:
					new_perm = list_perm + [c_n]
					perms.append(''.join(new_perm))

		return perms

print(len(all_perms('abcd')) == 4*3*2)