from flask import Blueprint, request, jsonify
from models import db, Produto, User

produto_bp = Blueprint('produto', __name__)
user_bp = Blueprint('user', __name__)

@produto_bp.route('/produtos', methods=['POST'])
def criar_produto():
    dados = request.json
    novo_produto = Produto(nome=dados['nome'])
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({'id': novo_produto.id, 'nome': novo_produto.nome}), 201

@produto_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([{'id': p.id, 'nome': p.nome} for p in produtos]), 200

@produto_bp.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    dados = request.json
    produto = Produto.query.get(id)
    
    if not produto:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    
    produto.nome = dados['nome']
    db.session.commit()
    return jsonify({'id': produto.id, 'nome': produto.nome}), 200

@produto_bp.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    produto = Produto.query.get(id)
    
    if not produto:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    
    db.session.delete(produto)
    db.session.commit()
    return jsonify({'mensagem': 'Produto deletado com sucesso'}), 200

@user_bp.route('/user/register', methods=['POST'])
def register_user():
    dados = request.json
    novo_user = User(nome=dados['nome'], senha=dados['senha'])
    db.session.add(novo_user)
    db.session.commit()
    return jsonify({'id': novo_user.id, 'nome': novo_user.nome, 'email': novo_user.email}), 201

@user_bp.route('/user/login', methods=['POST'])
def login_user():
    dados = request.json
    user = User.query.filter_by(nome=dados['nome'], senha=dados['senha']).first()
    
    if not user:
        return jsonify({'erro': 'Usuário não encontrado'}), 404
    
    return jsonify({'id': user.id, 'nome': user.nome, 'email': user.email}), 200
