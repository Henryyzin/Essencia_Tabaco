from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Pasta principal onde os currículos serão salvos
PASTA_BASE = 'curriculos'
os.makedirs(PASTA_BASE, exist_ok=True)  # Cria a pasta base se não existir

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cronograma')
def cronograma():
    return render_template('cronograma.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']
    area = request.form['area']  # 'eletrica' ou 'desenho'
    arquivo = request.files['curriculo']

    # Cria a subpasta com base na área
    subpasta = os.path.join(PASTA_BASE, f'curriculos_{area}')
    os.makedirs(subpasta, exist_ok=True)  # Cria a subpasta se não existir

    if arquivo:
        caminho = os.path.join(subpasta, arquivo.filename)
        arquivo.save(caminho)

    return render_template('obrigado.html', nome=nome, area=area.capitalize(), email=email)

if __name__ == '__main__':
    app.run(debug=True)
