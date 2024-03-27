import numpy as np
import matplotlib.pyplot as plt

from materials import *
from sources import *
num_bins = 100
bins = np.arange(1, num_bins + 1)

for material, data in materials.items():
    opacity = calculate_opacity(data["peak"], data["sigma"], bins)
    plt.plot(bins, opacity, label=material)

for source, data in sources.items():
    opacity = calculate_opacity(data["peak"], data["sigma"], bins)
    plt.plot(bins, opacity, label=source)

plt.xlabel('lambda')
plt.ylabel('normalized intensity')
plt.legend()
plt.grid(True)
plt.show()
