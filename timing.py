import graham_scan    # Import required modules
import jarvis_march
import monotone_chain
import time
import random

# Initialize empty lists to store x and y coordinates of points
x = []
y = []
# Define different sizes of points to test
size = [10, 50, 100, 500, 1000, 2000, 4000, 6000, 8000, 10000]
# Loop through each size
for n in size:
    # Initialize an empty list to store points
    points = []
    # Generate random points within the range [-1, 1] for x and y coordinates
    for p in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        new_point = [x, y]
        points.append(new_point)
        
    # Initialize total time counter
    total_time = 0
    # Perform 100 iterations for each algorithm
    for t in range(100):
        # Start measuring time
        start_time = time.perf_counter_ns()
        # Call the graham_scan algorithm to find the convex hull and make a copy of points
        graham_scan.find_convex_hull(points.copy())
        # End measuring time
        end_time = time.perf_counter_ns()
        # Calculate the time taken for each iteration
        total_time += end_time - start_time
    # Print the average time taken for each iteration of Graham Scan algorithm
    print("Graham Scan " + str(n) + " points: " + str(total_time/100) + " nanoseconds.")

    # Repeat the same process for Jarvis March algorithm
    total_time = 0
    for t in range(100):
        start_time = time.perf_counter_ns()
        jarvis_march.jarvis_march_convex_hull(points.copy())
        end_time = time.perf_counter_ns()
        total_time += end_time - start_time

    print("Jarvis March " + str(n) + " points: " + str(total_time/100) + " nanoseconds.")

    # Repeat the same process for Monotone Chain algorithm
    total_time = 0
    for t in range(100):
        start_time = time.perf_counter_ns()
        monotone_chain.monotone_chain(points.copy())
        end_time = time.perf_counter_ns()
        total_time += end_time - start_time

    print("Monotone Chain " + str(n) + " points: " + str(total_time/100) + " nanoseconds.\n")
