from flask import request, jsonify
from service.usuario_service import UsuarioService


class UsuarioController:
    @staticmethod
    def criar_usuario():
        data = request.get_json()
        cpf = data.get('cpf')
        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')
        
        if not cpf or not nome or not email or not senha:
            return jsonify({'erro': 'CPF, nome, email e senha são obrigatórios'}), 400
        
        usuario, mensagem = UsuarioService.criar_usuario(cpf, nome, email, senha)
        
        if usuario:
            return jsonify({'mensagem': mensagem, 'usuario': usuario.to_dict()}), 201
        else:
            return jsonify({'erro': mensagem}), 400
    
    @staticmethod
    def listar_todos():
        usuarios = UsuarioService.listar_todos()
        return jsonify([u.to_dict() for u in usuarios]), 200
    
    @staticmethod
    def buscar_por_cpf(cpf):
        usuario = UsuarioService.buscar_por_cpf(cpf)
        if usuario:
            return jsonify(usuario.to_dict()), 200
        else:
            return jsonify({'erro': 'Usuário não encontrado'}), 404
    
    @staticmethod
    def deletar_usuario(cpf):
        if UsuarioService.deletar_usuario(cpf):
            return jsonify({'mensagem': 'Usuário deletado com sucesso'}), 200
        else:
            return jsonify({'erro': 'Usuário não encontrado'}), 404


def usuario(app):
    app.add_url_rule('/usuarios', view_func=UsuarioController.criar_usuario, methods=['POST'])
    app.add_url_rule('/usuarios', view_func=UsuarioController.listar_todos, methods=['GET'])
    app.add_url_rule('/usuarios/<cpf>', view_func=UsuarioController.buscar_por_cpf, methods=['GET'])
    app.add_url_rule('/usuarios/<cpf>', view_func=UsuarioController.deletar_usuario, methods=['DELETE'])

