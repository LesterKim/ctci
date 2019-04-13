class Box:
	def __init__(self, height, width, depth):
		self.height = height
		self.width = width
		self.depth = depth


def max_height(boxes):
	return sum([box.height for box in max_stack(boxes)])

def is_a_box_bigger(a, b):
	return a.height > b.height and a.width > b.width and \
		a.depth > b.depth

def is_a_box_taller(a, b):
	return a.height > b.height and a.width > b.width and \
		a.depth > b.depth

def max_stack(boxes):
	n = len(boxes)

	if n < 2: return boxes

	last_box = boxes[n-1]
	sub_stack = max_stack(boxes[:n-1])

	for i, box in enumerate(sub_stack):
		if is_a_box_bigger(last_box, box):
			return sub_stack[:i] + [last_box] + sub_stack[i:]
		if last_box.height > box.height and 

n = 1000
boxes = [Box(i, i+1, i+2) for i in range(1,n+1)]

#print(max_height(boxes))
assert max_height(boxes) == (n+1)*n/2