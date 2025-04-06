from flask import Flask, render_template, request

import matplotlib.pyplot as plt
import math
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        v0 = float(request.form['v0'])
        angulo = float(request.form['angulo'])
        y0 = float(request.form['y0'])

        theta = math.radians(angulo)
        v0x = v0 * math.cos(theta)
        v0y = v0 * math.sin(theta)
        g = 9.8

        t_total = (v0y + math.sqrt(v0y**2 + 2 * g * y0)) / g
        tempos = [t / 100 for t in range(int(t_total * 100) + 1)]
        x = [v0x * t for t in tempos]
        y = [y0 + v0y * t - 0.5 * g * t**2 for t in tempos]

        plt.figure(figsize=(10, 5))
        plt.plot(x, y, color='green')
        plt.title('Trajetória do Lançamento Oblíquo')
        plt.xlabel('Distância (m)')
        plt.ylabel('Altura (m)')
        plt.grid(True)
        plt.ylim(bottom=0)


        caminho = os.path.join('static', 'trajeto.png')
        plt.savefig(caminho)
        plt.close()

        return render_template('index.html', imagem=caminho)

    return render_template('index.html', imagem=None)

if __name__ == '__main__':
    app.run(debug=True)
