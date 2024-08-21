import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm


def map_layer(map):
    return np.where(map % 10 == 1, 1, 0)

def sensor_layer(map):
    return np.where(map // 10, (map//10), 0)

def custom_colormap():
    # 254 colors from light pink to dark red
    colors = np.zeros((254, 4))
    for i in range(254):
        # Linearly interpolate RGB values
        # Start from light pink (255, 182, 193) to dark red (139, 0, 0)
        r = np.linspace(255, 139, 254)[i] / 255
        g = np.linspace(182, 0, 254)[i] / 255
        b = np.linspace(193, 0, 254)[i] / 255
        colors[i] = [r, g, b, 1]  # RGBA, where A is Alpha for opacity

    # Add white and gray at the start
    colors = np.vstack(([1, 1, 1, 1], [0.75, 0.75, 0.75, 1], colors))
    return ListedColormap(colors)

def sensor_plot(data):
    # Use the custom colormap
    cmap = custom_colormap()

    # Define the bounds and norm with specific attention to 0 and 1
    bounds = [0, 0.5, 1.5] + list(np.linspace(2, np.max(data), num=254))  # More fine-grained above 1
    norm = BoundaryNorm(bounds, cmap.N)
    # Plotting
    plt.imshow(data, cmap=cmap, norm=norm, interpolation='nearest')
    plt.title('2D Array Visualization with Custom Colormap')
    plt.show()
