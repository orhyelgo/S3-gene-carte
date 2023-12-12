from flask import Flask, render_template
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import noise
import io
import base64

app = Flask(__name__)

# ...

def generate_plot():
    # Générer le terrain de montagne
    terrain = generate_mountain(largeur, profondeur)

    # Créer une grille 2D pour les coordonnées X et Y
    x = np.arange(0, largeur, 1)
    y = np.arange(0, profondeur, 1)
    x, y = np.meshgrid(x, y)

    # Créer un tracé 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Tracer la montagne en 3D
    ax.plot_surface(x, y, terrain, cmap='terrain', linewidth=0, antialiased=False)

    # Sauvegarder la figure dans un objet BytesIO
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    # Fermer la figure pour libérer la mémoire
    plt.close()

    return plot_url

@app.route('/')
def index():
    plot_url = generate_plot()
    return render_template('index.html', plot_url=plot_url)

# ...
