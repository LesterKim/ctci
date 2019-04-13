from copy import deepcopy

def print_queens(n):
	print(boards)

def print_queen_boards():
	def is_safe(combo):
		for i in range(8):
			# Rows and columns
			if sum([combo[i][j] for j in range(8)]) > 1:
				return False
			if sum([combo[j][i] for j in range(8)]) > 1:
				return False

			# Diagonals
			if sum([combo[j+i][j] for j in range(8-i)]) > 1:
				return False
			if sum([combo[7-j-i][j] for j in range(8-i)]) > 1:
				return False

			if sum([combo[j][j+i] for j in range(8-i)]) > 1:
				return False
			if sum([combo[7-j][j+i] for j in range(8-i)]) > 1:
				return False

		return True

	def create_combos(n):
		combos = []

		if n == 1:
			for i in range(8):
				board = [[0 for i in range(8)] for i in range(8)]
				board[i][0] = 1
				combos.append(board)

			return combos

		sub_combos = create_combos(n-1)

		for sub_combo in sub_combos:
			for i in range(8):
				new_combo = deepcopy(sub_combo)
				new_combo[i][n-1] = 1

				if is_safe(new_combo):
					combos.append(new_combo)

		return combos


	for i, combo in enumerate(create_combos(8)):
		print("Combo %i" % i)
		for row in combo:
			print(row)

print_queen_boards()
#print(create_combos(1))