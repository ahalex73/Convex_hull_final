from graham_scan import cross_product as cross


def monotone_chain(points):
	# sort the points based on the x coordinate
	points.sort()

	# Build lower hull
	lower = []
	for p in points:
		while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
			lower.pop()
		lower.append(p)

	# Build upper hull
	upper = []
	for p in reversed(points):
		while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
			upper.pop()
		upper.append(p)

	# Return combined hull, ignore the last points in the list
	# as they are duplicates of the starting points in the lists
	hull = lower[:-1] + upper
	return hull



input_points = [(0,0),(0,4),(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,3),(2,3),(3,3),(4,4),(4,0)]
print(monotone_chain(input_points))