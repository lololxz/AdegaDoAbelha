from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

@app.route('/pagamento')
def pagamento():
    return render_template('pagamento.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/quem-somos')
def quem_somos():
    return render_template('quem_somos.html')

@app.route('/termos')
def termos():
    return render_template('termos.html')
