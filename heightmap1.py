import numpy as np
import matplotlib.pyplot as plt

def generate_heightmap(size, scale=1.0, seed=None):
    if seed is not None:
        np.random.seed(seed)

    # Générer une grille de points aléatoires
    heights = np.random.uniform(0, scale, size=(size, size))
    return heights

def plot_heightmap(heightmap):
    plt.imshow(heightmap, cmap='terrain', interpolation='bilinear')
    plt.colorbar()
    plt.show()

# Paramètres
map_size = 50 # Taille de la heightmap (carrée)
map_scale = 1000.0  # Échelle de la hauteur

# Générer et afficher la heightmap
heightmap = generate_heightmap(map_size, map_scale)
plot_heightmap(heightmap)