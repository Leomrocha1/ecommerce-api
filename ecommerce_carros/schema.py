from marshmallow import Schema, fields

class CarrosSchema(Schema):
    class Meta:
        """Class para ordenar os campos da classe CarrosSchema"""
        ordered = True
    """Schema para validar os dados de carros"""
    id = fields.Integer(dump_only=True)
    marca = fields.String(required=True, allow_none=False)
    modelo = fields.String(required=True, allow_none=True)
    ano_fabricacao = fields.Integer(required=True, allow_none=True)
    ano_modelo = fields.Integer(required=True, allow_none=True)
    km = fields.Integer(required=True, allow_none=True)
    cambio = fields.String(required=True, allow_none=True)
    combustivel = fields.String(required=True, allow_none=True)
    cor = fields.String(required=True, allow_none=True)
    valor = fields.Float(required=True, allow_none=True)
    descricao = fields.String(required=True, allow_none=True)
    criado_em = fields.DateTime(dump_only=True)