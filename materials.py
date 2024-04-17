import numpy as np

materials = {
    "bolognium": {"density": 7.85, "peak": 38.5, "sigma": 4.5, "a": 0.3, "b": 0.2},
    "turbonium": {"density": 2.7, "peak": 57.0, "sigma": 3.1, "a": 0.11, "b": 0.2},
    "spice_melange": {"density": 0.7, "peak": 27.0, "sigma": 7.8, "a": 0.62, "b": 0.7},
    "unobtanium": {"density": 2.5, "peak": 45.0, "sigma": 1.8, "a": 0.41, "b": 0.1},
    "lincoln": {"density": 1.0, "peak": 63.0, "sigma": 3.3, "a": 0.5, "b": 0.9},
    "mountain_dew": {"density": 1.0, "peak": 80.0, "sigma": 15.3, "a": 0.3, "b": 0.55},
    "jupiterium": {"density": 1.9, "peak": 50.0, "sigma": 50.0, "a": 0.01, "b": 0.22},
    "legos": {"density": 2.1, "peak": 10.0, "sigma": 6.3, "a": 0.3, "b": 0.6},
}

# Function to calculate opacity based on Gaussian function
def calculate_opacity(peak, sigma, x):
    return np.exp(-(x - peak)**2 / (2 * sigma**2))