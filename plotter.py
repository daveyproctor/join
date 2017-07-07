#!/usr/bin/env python3
import pickle
import sys
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import student join function
from join import join

def timer(fn, *args):
    start = time.time()
    fn(*args)
    end = time.time()
    return (end - start) * 1000

if __name__ == "__main__":
    # Load (deserialize) tables
    table1 = pickle.load(open("table1", "rb"))
    table2 = pickle.load(open("table2", "rb"))

    # Create list of input sizes
    sizes = list(range(100, 4600, 100))
    durations = []

    for size in sizes:
        print("Joining two tables with {} rows...".format(size), end="")
        duration = timer(join, table1[:size], table2[:size], "zip1", "zip2")
        print(" done. Duration: {} ms".format(duration))
        durations.append(duration)

    # Create figure and plot data
    plt.plot(sizes, durations, 'b')
    plt.xlabel("Rows in table")
    plt.ylabel("Time (ms)")
    plt.title("Time complexity of JOIN")
    plt.savefig("join.png", bbox_inches="tight")

