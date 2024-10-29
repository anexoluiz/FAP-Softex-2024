from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
from models import db, Usuario

login_bp = Blueprint('user', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    usuario = request.json.get('usuario', None)
    senha = request.json.get('senha', None)

    if not usuario or not senha:
        return jsonify({'erro': 'Faltam dados'}), 400
    
    usuarios = Usuario.query.all()
    if not any(u.nome == usuario and u.senha == senha for u in usuarios):
        return jsonify({'erro': 'Usuário ou senha inválidos'}), 401
    
    access_token = create_access_token(identity=usuario)
    return jsonify(access_token=access_token), 200
