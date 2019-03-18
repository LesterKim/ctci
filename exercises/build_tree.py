# Node
class Node:
	def __init__(self, value, children=[], visited=False):
		self.value = value
		self.children = children
		self.visited = visited

def build_tree(array, start, end):
	if start > end:
		return Node(None)

	mid = (start + end) // 2
	root = Node(array[mid])

	root.children.append(build_tree(array, start, mid-1))
	root.children.append(build_tree(array, mid+1, end))

	return root

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

root = build_tree(list(range(4)), 0, 3)

#print(root.children[1].value)
print(bfs(root))