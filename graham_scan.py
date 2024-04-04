import random
import math

# random.seed(1)

def conversion(oldlist):
    newlist = []
    for i in oldlist:
        newlist.append((i.x, i.y))
    return newlist


def slope(p1, p2):
    if p1[0] == p2[0]:
        return float('inf')
    else:
        return 1.0*(p1[1]-p2[1])/(p1[0]-p2[0])


def cross_product(p1, p2, p3):
    return ((p2[0] - p1[0])*(p3[1] - p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))


def find_convex_hull(list_of_points):
    """ Finds the smallest convex polyhedron/polygon containing
    all the points in a list """
    hull = []
    # list_of_points = conversion(list_of_points)
    list_of_points.sort()

    start = list_of_points.pop(0)
    hull.append(start)

    list_of_points.sort(key=lambda p: (slope(p,start), -p[1],p[0]))
    for pt in list_of_points:
        hull.append(pt)
        while len(hull) > 2 and cross_product(hull[-3],hull[-2],hull[-1]) < 0:
            hull.pop(-2)
    hull.append(hull[0])

    return hull

print(type(((0,0),(0,4),(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,3),(2,3),(3,3),(4,4),(4,0))))

# n = 100
# points = []

# for p in range(n):
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#     new_point = [x, y]
#     points.append(new_point)

#hull = find_convex_hull(points)
#print(hull)

# n = 10
# points = []
# for m in range(n):
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#     new_point = [x, y]
#     points.append(new_point)

# print(points)
# print("\n\n")
# hull = find_convex_hull(points)
# print(type(hull))

# hull = tuple(hull)
# print(type(hull))
