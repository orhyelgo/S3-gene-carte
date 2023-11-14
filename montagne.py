import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import noise

# Dimensions du terrain
largeur, profondeur = 100, 100

# Génère un terrain de montagne avec du bruit de Perlin
def generate_mountain(largeur, profondeur, scale=50.0, octaves=6, persistence=0.5, lacunarity=2.0, seed=1):
    mountain = np.zeros((largeur, profondeur))
    for i in range(largeur):
        for j in range(profondeur):
            mountain[i][j] = noise.pnoise2(i / scale,
                                          j / scale,
                                          octaves=octaves,
                                          persistence=persistence,
                                          lacunarity=lacunarity,
                                          repeatx=largeur,
                                          repeaty=profondeur,
                                          base=seed)
    return mountain

# Génère le terrain de la montagne
terrain = generate_mountain(largeur, profondeur)

# Crée une grille 2D pour les coordonnées X et Y
x = np.arange(0, largeur, 1)
y = np.arange(0, profondeur, 1)
x, y = np.meshgrid(x, y)

# Crée un tracé 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Trace la montagne en 3D
ax.plot_surface(x, y, terrain, cmap='terrain', linewidth=0, antialiased=False)

# Affiche le tracé 3D
plt.show()
