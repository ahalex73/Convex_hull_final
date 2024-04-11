import random
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

# Set seed for testing purposes
random.seed(1)


def slope(p1, p2):
    if p1[0] == p2[0]:
        return float('inf')
    else:
        return 1.0*(p1[1]-p2[1])/(p1[0]-p2[0])


def cross_product(p1, p2, p3):
    return ((p2[0] - p1[0])*(p3[1] - p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))


def graham_scan(list_of_points):
    """ Finds the smallest convex polyhedron/polygon containing
    all the points in a list """
    fig = plt.figure()
    metadata = dict(title='video', artist='S')
    writer = PillowWriter(fps=4, metadata=metadata)

    with writer.saving(fig, "graham_scan.gif", 150):

        hull = []
        list_of_points.sort()
        x = []
        y = []
        for u in list_of_points:
            x.append(u[0])
            y.append(u[1])
        plt.scatter(x, y)
        plt.title("Graham Scan")
        writer.grab_frame()
        plt.clf()
        start = list_of_points.pop(0)
        hull.append(start)

        list_of_points.sort(key=lambda p: (slope(p,start), -p[1],p[0]))

        for pt in list_of_points:
            hull.append(pt)
            while len(hull) > 2 and cross_product(hull[-3],hull[-2],hull[-1]) < 0:
                hull.pop(-2)
            plt.scatter(x, y)
            u = []
            b = []
            for p in hull:
                u.append(p[0])
                b.append(p[1])
            plt.plot(u, b, color="red")
            plt.title("Graham Scan")
            writer.grab_frame()
            plt.clf()
        hull.append(hull[0])
        u = []
        b = []
        for p in hull:
            u.append(p[0])
            b.append(p[1])
        plt.scatter(x, y)
        plt.plot(u, b, color="red")
        plt.title("Graham Scan")
        writer.grab_frame()
        plt.clf()
    return hull


def monotone_chain(points):
    fig = plt.figure()
    metadata = dict(title='video', artist='S')
    writer = PillowWriter(fps=4, metadata=metadata)

    with writer.saving(fig, "monotone_chain.gif", 150):
        # sort the points based on the x coordinate
        points.sort()

        x = []
        y = []
        for u in points:
            x.append(u[0])
            y.append(u[1])
        plt.scatter(x, y)
        plt.title("Monotone Chain")
        writer.grab_frame()
        plt.clf()

        # Build lower hull
        lower = []
        for p in points:
            while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
            plt.scatter(x, y)
            u = []
            b = []
            for p in lower:
                u.append(p[0])
                b.append(p[1])
            plt.plot(u, b, color="red")
            plt.title("Monotone Chain")
            writer.grab_frame()
            plt.clf()

        # Build upper hull
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
            plt.scatter(x, y)
            t = []
            l = []
            for p in upper:
                t.append(p[0])
                l.append(p[1])
            plt.plot(u, b, color="red")
            plt.plot(t, l, color="green")
            plt.title("Monotone Chain")
            writer.grab_frame()
            plt.clf()

        # Return combined hull, ignore the last point in the lower list
        # as it is a duplicate of the starting points in the upper list
        hull = lower[:-1] + upper
        return hull


def convex_direction(pStart, qMid, rEnd):
    """
    This function is to find orientation of ordered triplet (pStart, qMid, rEnd).
    Returns:
     - 0: Collinear
     - 1: Clockwise
     - 2: Counterclockwise
    """
    convex_val = (qMid[1] - pStart[1]) * (rEnd[0] - qMid[0]) - (qMid[0] - pStart[0]) * (rEnd[1] - qMid[1])
    if convex_val == 0:
        return 0  # Collinear
    return 1 if convex_val > 0 else 2  # Clockwise or Counterclockwise


def jarvis_march(points):
    """
    This Function is to compute the convex hull of a set of points using the Gift Wrapping Algorithm (Jarvis March).
    """
    fig = plt.figure()
    metadata = dict(title='video', artist='S')
    writer = PillowWriter(fps=8, metadata=metadata)

    with writer.saving(fig, "jarvis_march.gif", 150):

        n = len(points)
        points.sort()

        # Initialize result list
        hull = []
        x = []
        y = []
        for u in points:
            x.append(u[0])
            y.append(u[1])
        plt.scatter(x, y)
        plt.title("Jarvis March")
        writer.grab_frame()
        plt.clf()

        # Find the leftmost point
        left = min(range(n), key=lambda x: points[x][0])
        point = left
        q = 0
        v = 0
        while True:
            hull.append(point)
            plt.scatter(x, y)
            u = []
            b = []
            for idx in hull:
                a = points[idx][0]
                w = points[idx][1]
                u.append(a)
                b.append(w)
            plt.plot(u, b, color="green")
            plt.title("Jarvis March")
            writer.grab_frame()
            plt.clf()
            # Search for a point 'qMid' such that orientation(point, qMid, rEnd) is counterclockwise
            q = (point + 1) % n
            for r in range(n):
                plt.scatter(x, y)
                a = points[r][0]
                w = points[r][1]
                u.append(a)
                b.append(w)
                plt.plot(u, b, color="red")
                plt.title("Jarvis March")
                writer.grab_frame()
                plt.clf()
                u.pop()
                b.pop()
                if convex_direction(points[point], points[q], points[r]) == 2:
                    q = r

            point = q

            # If we looped back to the starting point, the hull is complete
            if point == left:
                break

        # Output result
        convex_hull = [points[i] for i in hull]
        points.sort()
        convex_hull.append(points[0])
        plt.scatter(x, y)
        u = []
        b = []
        for p in convex_hull:
            u.append(p[0])
            b.append(p[1])
        plt.plot(u, b, color="green")
        plt.title("Jarvis March")
        writer.grab_frame()
        plt.clf()

    return convex_hull


n = 30
points = []
for p in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    new_point = [x, y]
    points.append(new_point)

graham_scan(points.copy())
monotone_chain(points.copy())
jarvis_march(points.copy())
