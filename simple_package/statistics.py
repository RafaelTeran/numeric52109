###
## simple_package - Module statistics.py
## Basic statistics calculations
###

## Here I need functions to take in data and do the
## following:
##
## 1) Calculate the mean, median, and standard deviation. 
##
## 2) Display the result with a clear and pretty print 
##    statement.
##
## 3) Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4) Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5) Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.
##

import numpy as np
import graphics as gfx

def calculate_mean(data):
    """Calculate the mean of the data."""
    data = np.asarray(data)
    return np.mean(data)

def calculate_median(data):
    """Calculate the median of the data."""
    data = np.asarray(data)
    return np.median(data)

def calculate_std(data):
    """Calculate the standard deviation of the data."""
    data = np.asarray(data)
    return np.std(data)

def print_statistics(data):
    """Calculate and pretty print the mean, median, and standard deviation."""
    mean = calculate_mean(data)
    median = calculate_median(data)
    std = calculate_std(data)
    
    print(f"Statistics Summary:")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {std:.2f}")
    return mean, median, std

import random

if __name__ == "__main__":
    # Example usage with random data
    sample_data = [random.randint(1, 10) for _ in range(20)]
    print_statistics(sample_data)
    try:
        gfx.plot_histogram(sample_data)
    except ImportError as e:
        print(e)

