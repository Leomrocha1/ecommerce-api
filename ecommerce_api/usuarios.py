from flask import Blueprint, jsonify, request
from ecommerce_api.model import Usuarios
from ecommerce_api.schema import UsuarioSchema
from marshmallow.exceptions import ValidationError
from ecommerce_api import db

app = Blueprint('usuario', __name__, url_prefix='/v1/usuario')

@app.route('', methods=['POST'])
def criar_usuario():
    """
    Cria um novo usuário.
    """
    try:
        dados = UsuarioSchema().load(request.json)
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
    """
    Retorna todos os usuários.
    """
    usuarios = Usuarios.query.all()

    if not usuarios:
        return jsonify({'mensagem': 'Nenhum usuário encontrado.'})

    resultado = jsonify(UsuarioSchema().dump(usuarios, many=True))

    return resultado

@app.route('/<int:id>', methods=['GET'])
def get_usuario(id):
    """
    Retorna um usuário pelo ID.
    """
    usuario = Usuarios.query.get(id)

    if not usuario:
        return jsonify({'mensagem': 'Usuário não encontrado.'}), 404

    return jsonify(UsuarioSchema().dump(usuario))


@app.route('/<int:id>', methods=['PATCH'])
def atualizar_usuario(id):
    """
    Atualiza um usuário pelo ID.
    """
    usuario = Usuarios.query.get(id)

    if not usuario:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404

    try:
        dados = UsuarioSchema(partial=True).load(request.json)
    except ValidationError as err:
        return jsonify({'erros': err.messages}), 400

    for chave, valor in dados.items():
        setattr(usuario, chave, valor)

    db.session.commit()

    return jsonify(UsuarioSchema().dump(usuario))

@app.route('/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    usuario = Usuarios.query.get(id)

    if not usuario:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404

    try:
        db.session.delete(usuario)
        db.session.commit()
    except ValidationError as err:
        return jsonify({'erros': err.messages}), 500

    return jsonify({'mensagem': 'Usuário deletado com sucesso'}), 204