import random
import tkinter as tk
from tkinter import ttk

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import pickle

from PIL import Image

# Dimensions de la carte
largeur_carte = 10
hauteur_carte = 10

# Liste de biomes
biomes = ["Plaine", "Forêt", "Montagne"]

# Fonction pour générer une carte aléatoire
def generer_carte(largeur, hauteur):
    carte = []
    for y in range(hauteur):
        ligne = []
        for x in range(largeur):
            biome = random.choice(biomes)
            ligne.append(biome)
        carte.append(ligne)
    return carte

# Fonction pour afficher la carte
def afficher_carte(carte):
    for ligne in carte:
        print(" ".join(ligne))

# Génération de la carte
ma_carte = generer_carte(largeur_carte, hauteur_carte)

# Affichage de la carte
afficher_carte(ma_carte)






# Fonction appelée lorsque le bouton de génération est cliqué
def generer_monde():
    climat = climat_var.get()
    relief = relief_var.get()
    densite_population = densite_population_var.get()
    
    # Vous pouvez ici intégrer votre génération de monde avec les paramètres choisis

    # À la place, nous afficherons simplement les paramètres choisis
    resultat_label.config(text=f"Paramètres choisis:\nClimat: {climat}\nRelief: {relief}\nDensité de population: {densite_population}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Générateur de Monde Fictif")

# Label pour le choix du climat
climat_label = ttk.Label(fenetre, text="Climat:")
climat_label.pack()

# Menu déroulant pour le choix du climat
climat_var = tk.StringVar()
climat_menu = ttk.Combobox(fenetre, textvariable=climat_var, values=["Tropical", "Tempéré", "Arctique"])
climat_menu.pack()

# Label pour le choix du relief
relief_label = ttk.Label(fenetre, text="Relief:")
relief_label.pack()

# Menu déroulant pour le choix du relief
relief_var = tk.StringVar()
relief_menu = ttk.Combobox(fenetre, textvariable=relief_var, values=["Montagneux", "Plat", "Vallonné"])
relief_menu.pack()

# Label pour la densité de population
densite_population_label = ttk.Label(fenetre, text="Densité de population:")
densite_population_label.pack()

# Curseur pour régler la densité de population
densite_population_var = tk.DoubleVar()
densite_population_slider = ttk.Scale(fenetre, from_=0.1, to=1.0, variable=densite_population_var, orient="horizontal")
densite_population_slider.pack()

# Bouton de génération
generer_bouton = ttk.Button(fenetre, text="Générer Monde", command=generer_monde)
generer_bouton.pack()

# Label pour afficher les résultats
resultat_label = ttk.Label(fenetre, text="")
resultat_label.pack()

fenetre.mainloop()





#3eme partie







# Dimensions de la carte
largeur_carte = 50
hauteur_carte = 50

# Fonction de génération de topographie aléatoire
def generer_topographie(largeur, hauteur):
    topographie = np.random.rand(hauteur, largeur)
    return topographie

# Fonction de mise à jour de la carte
def update(val):
    ax.clear()
    topographie = generer_topographie(largeur_carte, hauteur_carte)
    ax.imshow(topographie, cmap='terrain')
    fig.canvas.draw_idle()

# Création de la figure et de l'axe
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

# Génération initiale de la topographie
topographie = generer_topographie(largeur_carte, hauteur_carte)
im = ax.imshow(topographie, cmap='terrain')

# Définition des paramètres des curseurs
axcolor = 'lightgoldenrodyellow'
ax_largeur = plt.axes([0.25, 0.01, 0.65, 0.03], facecolor=axcolor)
ax_hauteur = plt.axes([0.25, 0.06, 0.65, 0.03], facecolor=axcolor)

# Curseurs pour régler la largeur et la hauteur
s_largeur = Slider(ax_largeur, 'Largeur', 10, 100, valinit=largeur_carte)
s_hauteur = Slider(ax_hauteur, 'Hauteur', 10, 100, valinit=hauteur_carte)

# Fonctions de mise à jour des curseurs
s_largeur.on_changed(update)
s_hauteur.on_changed(update)

plt.show()






#4eme partie




# Fonction pour générer une carte aléatoire
def generer_carte(largeur, hauteur):
    # Ici, vous pouvez générer la carte de manière aléatoire ou avec vos propres données
    # Pour cet exemple, nous utilisons une carte vide
    carte = [[0 for _ in range(largeur)] for _ in range(hauteur)]
    return carte

# Fonction pour enregistrer une carte dans un fichier
def enregistrer_carte(carte, nom_fichier):
    with open(nom_fichier, 'wb') as fichier:
        pickle.dump(carte, fichier)

# Fonction pour charger une carte depuis un fichier
def charger_carte(nom_fichier):
    with open(nom_fichier, 'rb') as fichier:
        carte = pickle.load(fichier)
    return carte

# Générer une carte
ma_carte = generer_carte(10, 10)

# Enregistrer la carte dans un fichier
enregistrer_carte(ma_carte, "carte_generée.pkl")

# Charger la carte depuis un fichier
carte_chargee = charger_carte("carte_generée.pkl")

# Afficher la carte chargée
for ligne in carte_chargee:
    print(ligne)


#5eme partie



# Fonction pour générer une carte aléatoire
def generer_carte(largeur, hauteur):
    # Ici, vous pouvez générer la carte de manière aléatoire ou avec vos propres données
    # Pour cet exemple, nous utilisons une carte vide
    carte = [[(0, 0, 0) for _ in range(largeur)] for _ in range(hauteur)]
    return carte

# Fonction pour exporter la carte en tant qu'image PNG
def exporter_carte_png(carte, nom_fichier):
    largeur, hauteur = len(carte[0]), len(carte)
    image = Image.new("RGB", (largeur, hauteur))

    for x in range(largeur):
        for y in range(hauteur):
            pixel = carte[y][x]
            image.putpixel((x, y), pixel)

    image.save(nom_fichier, "PNG")

# Générer une carte
ma_carte = generer_carte(10, 10)

# Exporter la carte en tant qu'image PNG
exporter_carte_png(ma_carte, "carte.png")

print("La carte a été exportée en tant qu'image PNG.")

