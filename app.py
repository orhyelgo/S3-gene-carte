
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)












'''from flask import Flask, render_template
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from noise import snoise2
import random
import os

app = Flask(__name__)

# Déclarez seed en dehors de la fonction result pour qu'elle soit accessible partout dans le script
seed = None


def interpolate_color(value, color_map):
    value = max(0, min(1, value))
    index = int(value * (len(color_map) - 1))
    return np.array(color_map[index])

def generate_heightmap(width, height, scale, octaves, persistence, lacunarity, repeatx, repeaty, seed):
    heightmap = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            heightmap[i][j] = snoise2(i/scale, j/scale, octaves=octaves, persistence=persistence,
                                       lacunarity=lacunarity, repeatx=repeatx, repeaty=repeaty, base=seed)
    return (heightmap - np.min(heightmap)) / (np.max(heightmap) - np.min(heightmap))

def generate_colored_heightmap(heightmap, color_preset, beach_threshold, beach_color):
    colored_heightmap = np.zeros((width, height, 3))
    for i in range(width):
        for j in range(height):
            colored_heightmap[i][j] = interpolate_color(heightmap[i][j], color_preset)

    beach_mask = heightmap < beach_threshold
    colored_heightmap[beach_mask] = beach_color

    return colored_heightmap

@app.route('/', methods=['GET'])
def index():
    # Votre code de génération de heightmap va ici
    global seed
    seed = random.randint(0, 1000000)

    return render_template('index.html', seed=seed)

@app.route('/result', methods=['GET'])
def result():
    # Génération de la heightmap
    global seed
    width = 200
    height = 200
    scale = 125.0

    heightmap = generate_heightmap(width, height, scale, 6, 0.5, 2.0, 24, 24, seed)

    heightmap = (heightmap - np.min(heightmap)) / (np.max(heightmap) - np.min(heightmap))

    colors = [
        (0, 0, 0.5),
        (0, 0, 1),
        (0.8, 0.8, 0.2),
        (0.2, 0.8, 0.2),
        (0.5, 0.5, 0.5),
        (0.9, 0.9, 0.9),
    ]

    colored_heightmap = generate_colored_heightmap(heightmap, colors, 0.2, (0.8, 0.8, 0.2))

    # Enregistrez l'image générée dans le dossier 'static' pour que Flask puisse la servir
    image_filename = 'heightmap_image.png'
    plt.imsave(os.path.join('static', image_filename), colored_heightmap)

    # Retournez le rendu HTML avec le résultat
    return render_template('result.html', seed=seed)

if __name__ == '__main__':
    app.run(debug=True)'''
