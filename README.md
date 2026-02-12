# Projeto Fullstack - API de Usuários

API REST para gerenciamento de usuários desenvolvida com Flask seguindo a arquitetura MVC (Model-View-Controller).

## Tecnologias

- Python 3
- Flask 3.0.0

## Arquitetura

O projeto segue o padrão MVC:

- **Model** (`model/usuario_model.py`): Define a classe Usuario e armazena os dados em uma lista em memória
- **Service** (`service/usuario_service.py`): Contém a lógica de negócio (criar, listar, buscar, deletar)
- **Controller** (`controller/usuario_controller.py`): Gerencia as rotas HTTP e validações

## Estrutura do Projeto

```
projeto_fullstack/
├── app.py                          # Arquivo principal da aplicação
├── requirements.txt                # Dependências do projeto
├── postman_collection.json         # Collection do Postman para testes
├── model/
│   └── usuario_model.py           # Modelo de dados
├── service/
│   └── usuario_service.py         # Lógica de negócio
└── controller/
    └── usuario_controller.py      # Controladores e rotas
```

## Instalação

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute a aplicação:
```bash
python app.py
```

O servidor estará disponível em `http://127.0.0.1:5000`

## Endpoints da API

### Criar Usuário
- **URL**: `/usuarios`
- **Método**: `POST`
- **Body**:
```json
{
  "cpf": "12345678900",
  "nome": "João Silva",
  "email": "joao@email.com",
  "senha": "senha123"
}
```
- **Resposta de Sucesso** (201):
```json
{
  "mensagem": "Usuário criado com sucesso",
  "usuario": {
    "cpf": "12345678900",
    "nome": "João Silva",
    "email": "joao@email.com",
    "senha": "senha123"
  }
}
```

### Listar Todos os Usuários
- **URL**: `/usuarios`
- **Método**: `GET`
- **Resposta** (200):
```json
[
  {
    "cpf": "12345678900",
    "nome": "João Silva",
    "email": "joao@email.com",
    "senha": "senha123"
  }
]
```

### Buscar Usuário por CPF
- **URL**: `/usuarios/<cpf>`
- **Método**: `GET`
- **Exemplo**: `/usuarios/12345678900`
- **Resposta** (200):
```json
{
  "cpf": "12345678900",
  "nome": "João Silva",
  "email": "joao@email.com",
  "senha": "senha123"
}
```

### Deletar Usuário
- **URL**: `/usuarios/<cpf>`
- **Método**: `DELETE`
- **Exemplo**: `/usuarios/12345678900`
- **Resposta** (200):
```json
{
  "mensagem": "Usuário deletado com sucesso"
}
```

## Testando a API

### Com Postman
Importe o arquivo `postman_collection.json` no Postman para ter acesso a todas as requisições pré-configuradas.

### Com curl

Criar usuário:
```bash
curl -X POST http://127.0.0.1:5000/usuarios -H "Content-Type: application/json" -d "{\"cpf\": \"12345678900\", \"nome\": \"João Silva\", \"email\": \"joao@email.com\", \"senha\": \"senha123\"}"
```

Listar todos:
```bash
curl http://127.0.0.1:5000/usuarios
```

Buscar por CPF:
```bash
curl http://127.0.0.1:5000/usuarios/12345678900
```

Deletar:
```bash
curl -X DELETE http://127.0.0.1:5000/usuarios/12345678900
```

## Observações

- Os dados são armazenados em memória (lista Python), portanto serão perdidos ao reiniciar a aplicação
- Não há persistência em banco de dados
- O CPF é usado como identificador único
- Todos os campos (cpf, nome, email, senha) são obrigatórios
