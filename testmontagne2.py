import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Définir la taille de la carte
carte_largeur = 100
carte_hauteur = 100
# Générer des données pour la carte
x = np.arange(0, carte_largeur, 1)
y = np.arange(0, carte_hauteur, 1)
x, y = np.meshgrid(x, y)

# Générer des caractéristiques de la carte (plages, montagnes, océans, lac, etc.)
plages = 0.2 * np.exp(-(x - 25)**2 / (2 * 10**2) - (y - 25)**2 / (2 * 10**2))
montagnes = 0.5 * np.exp(-((x - 10)**2 + (y - 40)**2) / (2 * 15**2))
oceans = 0.1 * np.exp(-((x - 10)**2 + (y - 10)**2) / (2 * 20**2))
lac = 0.4 * np.exp(-((x - 35)**2 + (y - 15)**2) / (2 * 8**2))

# Combiner les caractéristiques pour obtenir la carte finale
carte_data = plages + montagnes + oceans + lac

# Transformer la carte en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extruder la carte 2D vers la troisième dimension (z)
ax.plot_surface(x, y, carte_data, cmap='terrain')

# Ajouter un titre à la carte 3D
ax.set_title('Carte du Monde Fictif - 3D avec Caractéristiques')

# Afficher la carte 3D
plt.show()
