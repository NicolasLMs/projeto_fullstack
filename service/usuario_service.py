from model.usuario_model import db
from model.usuario_model import Usuario
import requests
from flask import request, jsonify


class usuario_controller:
    @staticmethod
    def criar_usuario():
        data = request.get_json()
        usuario = Usuario(
                cnpj = data.get('cnpj'),
                email = data.get('email'),
                celular = data.get('celular')
            )
        db.session.add(usuario)
        db.session.commit()
        return jsonify({'mensagem': 'Usuário cadastrado com sucesso'}),201
    

    @staticmethod
    def listar_usuario():
        usuario = Usuario.query.all()
        return jsonify([{
           'id' : usuario.id,
           'cnpj': usuario.cnpj,
           'email' : usuario.email,
           'celular' : usuario.celular,
           'status' : usuario.status
           } for usuario in usuario
           ])
    


