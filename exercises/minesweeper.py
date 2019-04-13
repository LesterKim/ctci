from random import sample

class Square:
	def __init__(self, val, revealed=False):
		self.val = val
		self.revealed = revealed

	def select(self):
		self.revealed = True

	def show(self):
		return str(self.val) if self.revealed else ' '


class Board:
	def __init__(self, n, n_bombs=0):
		self.n = n
		self.n_bombs = n_bombs if n_bombs > 0 else n >> 1
		self.board = [[Square(0) for i in range(n)] for i in range(n)]
		self.revealed_count = 0

		bombs = sample(range(n**2), self.n_bombs)
		print(bombs)
		bombs = [(bomb//n, bomb%n) for bomb in bombs]

		for (i,j) in bombs:
			self.board[i][j].val = '*'

			rows = [-1, 0, 1]
			cols = [-1, 0, 1]

			for r in rows:
				for c in cols:
					if self.is_safe(i+r, j+c) and str(self.board[i+r][j+c].val).isdigit():
						self.board[i+r][j+c].val += 1

	def is_safe(self, i, j):
		return i >= 0 and i < self.n and j >= 0 and j < self.n

class Game:
	def __init__(self, n=10):
		self.n = n
		self.board = Board(n)
		self.move_count = 0
		self.active = True
		self.new_game(n)

	def new_game(self, n=10):
		self.n = n
		self.board = Board(n)
		self.move_count = 0
		self.active = True

		print("New game!\n")
		print("Move %i" % self.move_count)

		for row in self.board.board:
			print([c.show() for c in row])

	def play(self):
		def dfs(i, j):
			square = self.board.board[i][j]
			square.revealed = True
			self.board.revealed_count += 1

			rows = [-1, 0, 1]
			cols = [-1, 0, 1]

			for r in rows:
				for c in cols:
					if self.board.is_safe(i+r, j+c) and not self.board.board[i+r][j+c].revealed:
						if self.board.board[i+r][j+c].val == 0:
							dfs(i+r, j+c)
						else:
							self.board.board[i+r][j+c].revealed = True
							self.board.revealed_count += 1


		while self.active:
			coord = input('Give me a row and column separated by a space (e.g. 3 5): ').split()
			i = int(coord[0])
			j = int(coord[1])
			self.move_count += 1

			square = self.board.board[i][j]

			if square.val == '*':
				print('You stepped on a mine!')

				for r in self.board.board:
					print([str(c.val) for c in r])

				self.active = False
				break

			if square.val == 0 and not square.revealed:
				dfs(i, j)

			if not square.revealed:
				square.revealed = True
				self.board.revealed_count += 1

			if self.board.revealed_count == self.board.n**2 - self.board.n_bombs:
				active = False

				print('You win!')

				for r in self.board.board:
					print([str(c.val) for c in r])

				break

			print("Move %i" % self.move_count)

			for row in self.board.board:
				print([c.show() for c in row])


game = Game()
game.play()