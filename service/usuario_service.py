from model.usuario_model import Usuario, usuarios


class UsuarioService:
    @staticmethod
    def criar_usuario(cpf, nome, email, senha):
        if any(u.cpf == cpf for u in usuarios):
            return None, 'CPF já cadastrado'
        
        usuario = Usuario(cpf, nome, email, senha)
        usuarios.append(usuario)
        return usuario, 'Usuário criado com sucesso'
    
    @staticmethod
    def listar_todos():
        return usuarios
    
    @staticmethod
    def buscar_por_cpf(cpf):
        for usuario in usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None
    
    @staticmethod
    def deletar_usuario(cpf):
        for i, usuario in enumerate(usuarios):
            if usuario.cpf == cpf:
                usuarios.pop(i)
                return True
        return False
    


