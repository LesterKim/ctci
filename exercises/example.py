class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

a = Node(0, None)
b = Node(1, a)
c = Node(2, b)

print(a.data == 0)
print(a.next == None)
print(b.data == 1)
print(b.next == a)
print(c.data == 2)
print(c.next == b)