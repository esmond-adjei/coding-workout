#!/usr/bin/python3
import numpy as np

def generate_pareto_data(size: int, shape: float) -> np.ndarray:
    # Set scale parameter
    scale = 1.0

    # Generate Pareto distribution
    pareto_data = (np.random.default_rng().pareto(shape, size) + 1) * scale

    # Convert to integer
    pareto_data = pareto_data.astype(int)

    return pareto_data

pareto_data = generate_pareto_data(size=100, shape=2.0)
print(sorted(pareto_data))
