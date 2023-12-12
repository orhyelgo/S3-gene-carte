import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from noise import snoise2
import random

# Function to generate the heightmap
def generate_heightmap(width, height, scale, octaves, persistence, lacunarity, repeatx, repeaty, seed):
    heightmap = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            heightmap[i][j] = snoise2(i/scale, j/scale, octaves=octaves, persistence=persistence,
                                       lacunarity=lacunarity, repeatx=repeatx, repeaty=repeaty, base=seed)
    return (heightmap - np.min(heightmap)) / (np.max(heightmap) - np.min(heightmap))

# Function to interpolate colors based on elevation
def interpolate_color(value, color_map):
    value = max(0, min(1, value))
    index = int(value * (len(color_map) - 1))
    return np.array(color_map[index])

# Function to generate the colored heightmap
def generate_colored_heightmap(heightmap, color_preset, beach_threshold, beach_color):
    colored_heightmap = np.zeros((width, height, 3))
    for i in range(width):
        for j in range(height):
            colored_heightmap[i][j] = interpolate_color(heightmap[i][j], color_preset)
    
    beach_mask = heightmap < beach_threshold
    colored_heightmap[beach_mask] = beach_color
    
    return colored_heightmap

# Define color presets based on elevation
color_presets = {
    'Default': [
        (0, 0, 0.5),     # Deep water
        (0, 0, 1),       # Shallow water
        (0.8, 0.8, 0.2), # Beach
        (0.2, 0.8, 0.2), # Land
        (0.5, 0.5, 0.5), # Mountain
        (0.9, 0.9, 0.9), # Snow
    ],
    'Desert': [
        (0.8, 0.7, 0),   # Sand
        (0.8, 0.8, 0.2), # Beach
        (0.7, 0.5, 0.3), # Desert
        (0.5, 0.5, 0.5), # Mountain
    ],
    'Plain': [
        (0.5, 0.8, 0.5), # Plain color
    ],
}


# Set the size of the heightmap
width = 200
height = 200

# Set the scale of the noise (affects the level of detail)
scale = 125.0

# Set a random seed for the noise generation
seed = random.randint(0, 1000000)
random.seed(seed)
np.random.seed(seed)

# Generate the heightmap using Perlin noise
heightmap = np.zeros((width, height))
for i in range(width):
    for j in range(height):
        heightmap[i][j] = snoise2(i/scale, j/scale, octaves=6, persistence=0.5, lacunarity=2.0, repeatx=24, repeaty=24, base=seed)

# Normalize the values to the range [0, 1]
heightmap = (heightmap - np.min(heightmap)) / (np.max(heightmap) - np.min(heightmap))

# Define color gradients based on elevation
colors = [
    (0, 0, 0.5),     # Deep water
    (0, 0, 1),       # Shallow water
    (0.8, 0.8, 0.2), # Beach
    (0.2, 0.8, 0.2), # Land
    (0.5, 0.5, 0.5), # Mountain
    (0.9, 0.9, 0.9), # Snow
]

# Interpolate colors based on elevation
def interpolate_color(value, color_map):
    value = max(0, min(1, value))
    index = int(value * (len(color_map) - 1))
    return np.array(color_map[index])

# Generate colored heightmap
colored_heightmap = np.zeros((width, height, 3))
for i in range(width):
    for j in range(height):
        colored_heightmap[i][j] = interpolate_color(heightmap[i][j], colors)

# Add a beach based on elevation threshold
beach_threshold = 0.2
beach_color = (0.8, 0.8, 0.2)  # Color for the beach

beach_mask = heightmap < beach_threshold
colored_heightmap[beach_mask] = beach_color



# User input for color preset
print("Available color presets:")
for preset_name in color_presets.keys():
    print(f"- {preset_name}")

selected_preset = input("Choose a color preset: ")

# Check if the selected preset exists, otherwise use the default preset
color_preset = color_presets.get(selected_preset, color_presets['Default'])

# Generate the colored heightmap using user-defined parameters and color preset
colored_heightmap = generate_colored_heightmap(heightmap, color_preset, beach_threshold, beach_color)

# Display the colored heightmap in 2D
plt.imshow(colored_heightmap, origin='lower')
plt.title(f'2D Colored Heightmap with Beach (Seed: {seed}, Preset: {selected_preset})')
plt.show()

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate x, y coordinates
x, y = np.meshgrid(np.arange(width), np.arange(height))

# Display the colored heightmap in 3D
ax.plot_surface(x, y, heightmap, facecolors=colored_heightmap, rstride=1, cstride=1, antialiased=True, shade=True)

# Display the plot
plt.title(f'3D Colored Heightmap with Beach (Seed: {seed}, Preset: {selected_preset})') 
plt.show()
