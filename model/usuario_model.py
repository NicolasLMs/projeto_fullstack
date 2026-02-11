usuarios = []

class Usuario:
    def __init__(self, cpf, nome, email, senha):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def to_dict(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha
        }
