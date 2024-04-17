# this code does a ridiculously fake optical transport of a binned source 
# through some fake opacities to produce an output spectrum

import numpy as np
import matplotlib.pyplot as plt
from materials import materials
from sources import sources

# Function to calculate opacity based on Gaussian function
def calculate_opacity(peak, sigma, x):
    return np.exp(-(x - peak)**2 / (2 * sigma**2))

# Function to calculate absorption through a material
def calculate_absorption(source_spectrum, shell_thicknesses):
    abs_result = []
    i = 0
    for material, drad in shell_thicknesses.items():
        peak = materials[material]["peak"]
        sigma = materials[material]["sigma"]
        
        if i > 0:
            key, value = list(shell_thicknesses.items())[i-1]
            a = materials[key]["a"]*value/15.0
            b = materials[key]["b"]*value/15.0
            print(a,b,(1-0.8*a+0.7*b)**2,(1-0.3*a+0.2*b)**3)
            peak = peak * (1-0.8*a+0.7*b)**2
            sigma = sigma * (1-0.3*a+0.2*b)**3
        opacity = calculate_opacity(peak, sigma, bins)
        density = materials[material]["density"]
        absorption = np.exp(-drad * opacity * density * 0.01)
        abs_result.append(absorption)
        i+=1
    return np.array(abs_result)

# Function to calculate source spectrum based on Gaussian function
def calculate_source_spectrum(brightness, peak, sigma, x):
    return brightness * np.exp(-(x - peak)**2 / (2 * sigma**2))

# Function to compute output spectrum
def compute_output_spectrum(source_spectrum, absorption_results):
    output_spectrum = source_spectrum.copy()
    for absorption in absorption_results:
        output_spectrum *= absorption
    return output_spectrum

num_bins = 100
bins = np.arange(1, num_bins + 1)

from setup import *

source_name = source
source_data = sources[source_name]
source_spectrum = calculate_source_spectrum(source_data["brightness"], source_data["peak"], source_data["sigma"], bins)

# Calculate absorption through each material
absorption_results = calculate_absorption(source_spectrum, shells)

# Compute output spectrum
output_spectrum = compute_output_spectrum(source_spectrum, absorption_results)

# Plot the results
plt.plot(bins, output_spectrum, label="Output Spectrum")
plt.xlabel('Bins')
plt.ylabel('Intensity')
plt.title('Output Spectrum after Absorption through Materials')
plt.legend()
plt.grid(True)
plt.show()

# Output 25 evenly spaced values from the output spectrum
evenly_spaced_indices = np.linspace(0, len(output_spectrum) - 1, 25, dtype=int)
evenly_spaced_values = output_spectrum[evenly_spaced_indices]

print("25 Evenly Spaced Values from the Output Spectrum:")
print(evenly_spaced_values.tolist())