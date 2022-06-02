from flask import Blueprint, jsonify, request
from ecommerce_api.model import Usuarios
from ecommerce_api.schema import UsuarioSchema
from marshmallow.exceptions import ValidationError
from ecommerce_api import db

app = Blueprint('usuario', __name__, url_prefix='/v1/usuario')

@app.route('', methods=['POST'])
def criar_usuario():
    try:
        dados = UsuarioSchema.load(request.json)
        print(dados)
    except ValidationError as err:
        return jsonify({'erros': err.messages}), 400

    usuario = Usuarios(**dados)

    try:
        db.session.add(usuario)
        db.session.commit()
    except ValidationError as err:
        return jsonify({'erros': err.messages}), 500

    return jsonify(UsuarioSchema().dump(usuario)), 201

@app.route('', methods=['GET'])
def get_usuarios():
    usuarios = Usuarios.query.all()

    if not usuarios:
        return jsonify({'mensagem': 'Nenhum usuário encontrado.'})

    resultado = jsonify(UsuarioSchema().dump(usuarios, many=True))

    return resultado