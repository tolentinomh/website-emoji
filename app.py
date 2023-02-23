import os
import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Ruta de la carpeta que contiene las imágenes
    img_dir = os.path.join(app.static_folder, 'img')

    # Lista de nombres de archivo de imágenes
    img_names = os.listdir(img_dir)

    # Selecciona una imagen al azar
    selected_img = random.choice(img_names)

    # Ruta de la imagen seleccionada
    img_path = os.path.join('img', selected_img)

    # Renderiza el template index.html con la imagen seleccionada
    return render_template('index.html', img_path=img_path)

if __name__ == '__main__':
    app.run()

