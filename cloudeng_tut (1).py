# Cloud Eng Tutorial
# https://aaltoscicomp.github.io/python-for-scicomp/parallel-pi-multiprocessing/

import numpy as np
import random
import time
import multiprocessing.pool


def sample(n):
    """Make n trials of points in the square.  Return (n, number_in_circle)
    
    This is our basic function.  By design, it returns everything it\
    needs to compute the final answer: both n (even though it is an input
    argument) and n_inside_circle.  To compute our final answer, all we
    have to do is sum up the n:s and the n_inside_circle:s and do our
    computation"""
    n_inside_circle = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 < 1.0:
            n_inside_circle += 1
    return n, n_inside_circle


print("Single Thread Calculations")
start = time.time()
# Do the actual calculation (the previous result doesn't get saved)
n, n_inside_circle = sample(10**6)
pi = 4.0 * (n_inside_circle / n)
pi

end = time.time()
print("Elapsed time" + str(end - start))


print("Multiprocessing Calculations")

pool = multiprocessing.pool.Pool()

start = time.time()
# Do the actual calculation (the previous result doesn't get saved)
results = pool.map(sample, [10**5] * 10)
pool.close()
n_sum = sum(x[0] for x in results)
n_inside_circle_sum = sum(x[1] for x in results)
pi = 4.0 * (n_inside_circle_sum / n_sum)
pi

end = time.time()
print("Elapsed time for multiprocessing" + str(end - start))


print("Parallel in threads Calculations")
threadpool = multiprocessing.pool.ThreadPool()

start = time.time()
results = threadpool.map(sample, [10**5] * 10)
threadpool.close()
n_sum = sum(x[0] for x in results)
n_inside_circle_sum = sum(x[1] for x in results)
pi = 4.0 * (n_inside_circle_sum / n_sum)
pi

end = time.time()
print("Elapsed time for multithreading" + str(end - start))

