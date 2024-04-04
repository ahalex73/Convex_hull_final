"""
This file is responsible for parsing test data from different files into a list of points.
"""
from graham_scan import *


file = open("eclipse_text_points.csv", "r")
i = 1
list_of_points = []

for line in file:
    x,y = line.split(',')
    x = float(x)
    y = float(y)
    list_of_points.append((x,y))

    i += 1


print(list_of_points)

# ch = find_convex_hull(list_of_points)
# print(ch)
