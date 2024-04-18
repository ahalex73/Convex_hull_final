
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
    list_of_points.sort()

    start = list_of_points.pop(0)
    hull.append(start)

    for pt in list_of_points:
        hull.append(pt)
        while len(hull) > 2 and cross_product(hull[-3], hull[-2], hull[-1]) < 0:
            hull.pop(-2)
    hull.append(hull[0])

    return hull
