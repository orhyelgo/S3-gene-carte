import numpy as np
import matplotlib.pyplot as plt
import noise
from mpl_toolkits.mplot3d import Axes3D

# Définir les dimensions du terrain
width = 100
height = 100



# Générer la grille de hauteur avec du bruit de Perlin
terrain = np.zeros((height, width))

# Paramètres de bruit
scale = 100.0  # Plus ce nombre est élevé, plus les caractéristiques seront grandes
octaves = 6  # Le nombre de couches de bruit à combiner
persistence = 0.5  # L'amplitude des octaves (diminue chaque octave)
lacunarity = 2.0  # La fréquence des octaves (augmente chaque octave)

# Générer le bruit de Perlin sur le terrain
for i in range(height):
    for j in range(width):
        terrain[i][j] = noise.pnoise2(i/scale, 
                                 j/scale, 
                                 octaves=octaves, 
                                 persistence=persistence, 
                                 lacunarity=lacunarity, 
                                 repeatx=1024, 
                                 repeaty=1024, 
                                 base=0)

# Normalisation du terrain pour obtenir des valeurs entre 0 et 1
terrain = (terrain - np.min(terrain)) / (np.max(terrain) - np.min(terrain))

# Définition des biomes en fonction de la hauteur
biome_colors = {
    'eau': [0, 0, 0.5],
    'plage': [0.9, 0.9, 0.2],
    'forêt': [0, 0.5, 0],
    'montagne': [0.5, 0.5, 0.5],
    'neige': [0.9, 0.9, 0.9]
}

# Appliquer les couleurs des biomes au terrain
colored_terrain = np.zeros((height, width, 3))
for i in range(height):
    for j in range(width):
        if terrain[i][j] < 0.2:
            colored_terrain[i][j] = biome_colors['eau']
        elif terrain[i][j] < 0.3:
            colored_terrain[i][j] = biome_colors['plage']
        elif terrain[i][j] < 0.6:
            colored_terrain[i][j] = biome_colors['forêt']
        elif terrain[i][j] < 0.8:
            colored_terrain[i][j] = biome_colors['montagne']
        else:
            colored_terrain[i][j] = biome_colors['neige']

# Afficher le terrain
plt.figure(figsize=(8, 8))
plt.imshow(colored_terrain)
plt.axis('off')  # Cacher les axes
plt.show()


# Création des grilles pour les axes X et Y
x = np.linspace(0, 1, width)
y = np.linspace(0, 1, height)
x, y = np.meshgrid(x, y)

# Utilisation des données de hauteur pour l'axe Z
z = terrain

# Création de la figure 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Tracer la surface 3D avec coloration en fonction de la hauteur
surface = ax.plot_surface(x, y, z, facecolors=colored_terrain)

# Cacher les axes pour une meilleure visualisation
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Afficher la figure
plt.show()

