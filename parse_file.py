"""
This file is responsible for parsing test data from different files into a list of points.
"""
# Import the graham_scan module
from graham_scan import *

def parse_file_for_known_convex_hull(file_name):
    # Open the file for reading
    file = open(file_name, "r")
    i = 1
    # Initialize an empty list to store points
    list_of_points = []
    # Iterate over each line in the file
    for line in file:
        # Split the line into x and y coordinates
        x,y = line.split(',')
        # Convert x and y coordinates to float
        x = float(x)
        y = float(y)
        # Append the coordinates as a tuple to the list
        list_of_points.append((x,y))

        # Increment the counter
        i += 1


    return list_of_points
    
# Call the function to parse the file for eclipse points and store the result
eclipse_points = parse_file_for_known_convex_hull("eclipse_text_points.csv")
# Call the function to parse the file for star points and store the result
star_points = parse_file_for_known_convex_hull("star_text_points.csv")
# Print the collected points for the eclipse shape
print(eclipse_points, "\n")
# Print the collected points for the star shape
print(star_points)
