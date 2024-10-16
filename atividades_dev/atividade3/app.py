from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

produtos = []

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    produto = request.form.get('produto')
    estoque = request.form.get('estoque')
    if produto and estoque:
        produtos.append({'nome': produto, 'estoque': estoque})
    return redirect(url_for('index'))

@app.route('/editar/<int:index>', methods=['POST'])
def editar(index):
    produto = request.form.get('produto')
    estoque = request.form.get('estoque')
    if 0 <= index < len(produtos) and produto and estoque:
        produtos[index] = {'nome': produto, 'estoque': estoque}
    return redirect(url_for('index'))

@app.route('/excluir/<int:index>')
def excluir(index):
    if 0 <= index < len(produtos):
        produtos.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
