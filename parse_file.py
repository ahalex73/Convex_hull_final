"""
This file is responsible for parsing test data from different files into a list of points.
"""
from graham_scan import *

def parse_file_for_known_convex_hull(file_name):
    file = open(file_name, "r")
    i = 1
    list_of_points = []

    for line in file:
        x,y = line.split(',')
        x = float(x)
        y = float(y)
        list_of_points.append((x,y))

        i += 1


    return list_of_points

eclipse_points = parse_file_for_known_convex_hull("eclipse_text_points.csv")
star_points = parse_file_for_known_convex_hull("star_text_points.csv")
print(eclipse_points, "\n")
print(star_points)
