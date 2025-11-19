###
## simple_package - Module graphics.py
## Basic graphics for statistics
###

import statistics as stats
import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

def plot_histogram(data):
    """Plot a histogram of the data with mean and median marked."""
    if plt is None:
        raise ImportError("matplotlib is not installed. Cannot plot histogram.")
    
    data = np.asarray(data)
    mean = np.mean(data)
    median = np.median(data)
    plt.figure(figsize=(10, 6))
    counts, bin_edges, patches = plt.hist(data, bins=20, alpha=0.7, color='blue', edgecolor='black')
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    plt.axvline(mean, color='red', linestyle='dashed', linewidth=1,
                  label='Mean')
    plt.axvline(median, color='green', linestyle='dashed',
                  linewidth=1, label='Median')
    
    visible_centers = bin_centers[counts > 0]
    tick_labels = [str(int(round(c))) for c in visible_centers]
    plt.xticks(visible_centers, tick_labels) 
    plt.xlim(1, 10) 
    plt.title('Histogram with Mean and Median')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()