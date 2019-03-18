# Node
class Node:
	def __init__(self, value, children=[], visited=False):
		self.value = value
		self.children = children
		self.visited = visited

def is_balanced(root):
	children = root.children

	if len(children) == 0:
		return True
	elif len(children) == 1:
		return len(children[0].children) == 0
	else:
		[l, r] = children
		return is_balanced(l) and is_balanced(r) and abs(height(l) - height(r)) < 2

def height(root):
	children = root.children

	if len(children) == 0:
		return 0
	else:
		return max(height(children[0]), height(children[1])) + 1

f = Node(6)
e = Node(5)
d = Node(4)
c = Node(3)
b = Node(2, [e, f])
a = Node(1, [c, d])
root = Node(0, [a, b])

print(is_balanced(root))

h = Node(2)
g = Node(1, [h])
root2 = Node(0, [g])

print(is_balanced(root2))