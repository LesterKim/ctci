def route(node1, node2):
	return BFS(node1, node2) or BFS(node2, node1)

def BFS(node1, node2):
	node1.visited = True
	queue = [node1]

	while len(queue) > 0:
		r = queue.pop(0)

		if r == node2:
			return True

		for child in r.children:
			if not child.visited:
				child.visited = True
				queue.append(child)

# Nodes
class Node:
	def __init__(self, value, children=[], visited=False):
		self.value = value
		self.children = children
		self.visited = visited

f = Node(6)
e = Node(5)
d = Node(4)
c = Node(3)
b = Node(2, [e, f])
a = Node(1, [c, d])
root = Node(0, [a, b])

print(route(root, f))
print(route(f, a))