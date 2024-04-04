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


def jarvis_march_convex_hull(points):
    """
    This Function is to compute the convex hull of a set of points using the Gift Wrapping Algorithm (Jarvis March).
    """
    n = len(points)
    if n < 3:
        return print("Convex hull not possible")

    # Initialize result list
    hull = []

    # Find the leftmost point
    left = min(range(n), key=lambda x: points[x][0])
    point = left
    q = 0

    while True:
        hull.append(point)

        # Search for a point 'qMid' such that orientation(point, qMid, rEnd) is counterclockwise
        q = (point + 1) % n
        for r in range(n):
            if convex_direction(points[point], points[q], points[r]) == 2:
                q = r

        point = q

        # If we looped back to the starting point, the hull is complete
        if point == left:
            break

    # Output result
    convex_hull = [points[i] for i in hull]
    convex_hull.append(points[0])

    return convex_hull


# def main():
#     points = [(0,0),(0,4),(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,3),(2,3),(3,3),(4,4),(4,0)]
#     points2 = [(0, 0), (1, 4), (3, 1), (3, 3), (5, 2), (5, 5), (7, 0), (9, 6)]
#     print("Convex Hull 1:", jarvis_march_convex_hull(points))
#     print("Convex Hull 2:", jarvis_march_convex_hull(points2))
#     print("This is considered a Convex Hull from the given points")


# if __name__ == "__main__":
#     main()
