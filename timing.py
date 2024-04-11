import graham_scan
import jarvis_march
import monotone_chain
import time
import random

x = []
y = []
size = [10, 50, 100, 500, 1000, 2000, 4000, 6000, 8000, 10000]
for n in size:
    points = []
    for p in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        new_point = [x, y]
        points.append(new_point)

    total_time = 0
    for t in range(100):
        start_time = time.perf_counter_ns()
        graham_scan.find_convex_hull(points.copy())
        end_time = time.perf_counter_ns()
        total_time += end_time - start_time

    print("Graham Scan " + str(n) + " points: " + str(total_time/100) + " nanoseconds.")

    total_time = 0
    for t in range(100):
        start_time = time.perf_counter_ns()
        jarvis_march.jarvis_march_convex_hull(points.copy())
        end_time = time.perf_counter_ns()
        total_time += end_time - start_time

    print("Jarvis March " + str(n) + " points: " + str(total_time/100) + " nanoseconds.")

    total_time = 0
    for t in range(100):
        start_time = time.perf_counter_ns()
        monotone_chain.monotone_chain(points.copy())
        end_time = time.perf_counter_ns()
        total_time += end_time - start_time

    print("Monotone Chain " + str(n) + " points: " + str(total_time/100) + " nanoseconds.\n")
