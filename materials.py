import numpy as np

materials = {
    "bolognium": {"density": 7.85, "peak": 38.5, "sigma": 4.5},
    "turbonium": {"density": 2.7, "peak": 57.0, "sigma": 3.1},
    "spice_melange": {"density": 0.7, "peak": 27.0, "sigma": 7.8},
    "unobtanium": {"density": 2.5, "peak": 45.0, "sigma": 1.8},
    "lincoln": {"density": 1.0, "peak": 63.0, "sigma": 3.3},
    "mountain_dew": {"density": 1.0, "peak": 80.0, "sigma": 15.3},
    "jupiterium": {"density": 1.9, "peak": 50.0, "sigma": 50.0},
    "legos": {"density": 2.1, "peak": 10.0, "sigma": 6.3},
}

# Function to calculate opacity based on Gaussian function
def calculate_opacity(peak, sigma, x):
    return np.exp(-(x - peak)**2 / (2 * sigma**2))