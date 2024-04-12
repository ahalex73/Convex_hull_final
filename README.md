# Convex_hull_final
CS4310 - Design and Analysis of Algorithms Convex Hull Project
Skyler Dare
Alexander Holmes
Tyler Hitchcock


# Packages needed
Matplotlib - For graphing points out

Math - For using math related functionality

Pytest - For testing - showing assertions are met

Time - For measuring execution time of functions


# Use of each file
graham_scan.py - Implementation of convex hull algorithm called graham scan

monotone_chain.py - Implementation of convex hull algorithm called monotone chain scan

jarvis_march.py - Implementation of convex hull algorithm called Jarvis march scan

generate_points.py - Generates a listing of points to run for n-timing functions

parse_file.py - Allows the parsing of CSV files

visualizer.py - Creates GIF files that demonstrate the calculating steps of each algorithm, as well as generate a timing graph for comparing each algorithm.

# Use of each CSV file
star_text_points.csv    - contains known convex hull of star

eclipse_text_points.csv - contains known convex hull of eclipse



# How to run program
Use your favorite python IDE, either parse your points into a points list using the CSV parser file, 
or generate random ones using the generate_random_points function in the graham scan file. Then run 
any of the three implementations of convex hull on it.

