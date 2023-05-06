#!/usr/bin/python3
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')

def generate_pareto_data(size: int, shape: float) -> np.ndarray:
    # Set scale parameter
    scale = 1.0

    # Generate Pareto distribution
    pareto_data = (np.random.default_rng().pareto(shape, size) + 1) * scale

    # Convert to integer
    pareto_data = pareto_data.astype(int)

    return pareto_data

def plot_pareto_histogram(data: np.ndarray):
    # Plot histogram
    plt.hist(data, bins=range(min(data), max(data) + 2, 1), align='left', rwidth=0.8)

    # Set axis labels
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # Show plot
    plt.show()

# Generate Pareto data
pareto_data = generate_pareto_data(size=1000, shape=2.0)

# Plot histogram
plot_pareto_histogram(pareto_data)
plot_pareto_histogram([a*0.9 for a in pareto_data])
