###
## simple_package - Module graphics.py
## Basic graphics for statistics
###

import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

def plot_histogram(data, a, b):
    """Plot a histogram of the data with mean and median marked."""
    if plt is None:
        raise ImportError("matplotlib is not installed. Cannot plot histogram.")
    
    data = np.asarray(data)
    mean = data.mean()
    median = np.median(data)

    mn, mx = data.min(), data.max()

    bins = np.arange(mn - 0.5, mx + 0.5 + 1, 1)

    plt.figure(figsize=(8, 4))
    counts, edges, patches = plt.hist(
        data,
        bins=bins,
        edgecolor='black',
        alpha=0.7,
        align='mid'
    )

    plt.axvline(mean, color='red', linestyle='--', linewidth=1,
                label=f"Mean: {mean:.2f}")
    plt.axvline(median, color='green', linestyle='--', linewidth=1,
                label=f"Median: {median:.2f}")
    # Mark the x-axis ticks
    plt.xticks(np.arange(mn, mx + 1))
    # This ensures the x-axis limits are set according to provided a and b
    plt.xlim(a - 0.5, b + 0.5)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Data')
    plt.legend()
    plt.show()