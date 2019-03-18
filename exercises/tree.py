# Tree
class Tree:
	def__init__(self, nodes):
		self.nodes = nodes

# Node
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

# BFS
def bfs(node):
	node.visited = True
	queue = [node]

	while len(queue) > 0:
		r = queue.pop(0)
		print(r.value)

		for child in r.children:
			if not child.visited:
				child.visited = True
				queue.append(child)

print(bfs(root))


# DFS
def dfs(node):
	if not node.visited:
		node.visited = True
		print(node.value)

		for child in node.children:
			dfs(child)

#print(dfs(root))