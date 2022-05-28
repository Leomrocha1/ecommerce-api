import logging
from flask import Blueprint, jsonify, request
from ecommerce_carros.model import Carros
from ecommerce_carros.schema import CarrosSchema
from marshmallow.exceptions import ValidationError
from ecommerce_carros import db

LOGGER = logging.getLogger(__name__)

app = Blueprint('carro', __name__, url_prefix='/v1/carro')


@app.route('', methods=['GET'])
def get_carros():
    """
    Retorna todos os carros.
    """
    carros = Carros.query.all()

    if not carros:
        return jsonify({'mensagem': 'Nenhum carro cadastrado.'}), 404

    resultado = jsonify(CarrosSchema().dump(carros, many=True))

    return resultado


@app.route('/<int:id>', methods=['GET'])
def get_carro(id):
    """
    Retorna um carro pelo id.
    """
    carro = Carros.query.get(id)

    if not carro:
        return jsonify({'mensagem': 'Carro não encontrado.'}), 404

    resultado = jsonify(CarrosSchema().dump(carro))

    return resultado


@app.route('', methods=['POST'])
def criar_carro():
    """
    Cria um novo carro.
    """
    try:
        dados = CarrosSchema().load(request.json)
    except ValidationError as err:
        return jsonify({'erros': err.messages}), 400

    carro = Carros(**dados)

    try:
        db.session.add(carro)
        db.session.commit()
    except ValidationError as err:
        return jsonify({'erros': err.messages}), 500


    return jsonify(CarrosSchema().dump(carro)), 201


@app.route('/<int:id>', methods=['PATCH'])
def atualizar_carro(id):
    """
    Atualiza um carro pelo id.
    """
    carro = Carros.query.get(id)

    if not carro:
        return jsonify({'mensagem': 'Carro não encontrado'}), 404

    try:
        dados = CarrosSchema(partial=True).load(request.json)
    except ValidationError as err:
        return jsonify({'erros': err.messages}), 400

    for chave, valor in dados.items():
        setattr(carro, chave, valor)

    db.session.commit()

    return jsonify(CarrosSchema().dump(carro))


@app.route('/<int:id>', methods=['DELETE'])
def deletar_carro(id):
    carro = Carros.query.get(id)

    if not carro:
        return jsonify({'mensagem': 'Carro não encontrado'}), 404

    try:
        db.session.delete(carro)
        db.session.commit()
    except ValidationError as err:
        return jsonify({'erros': err.messages}), 500

    return jsonify({'mensagem': 'Carro deletado com sucesso'}), 204
