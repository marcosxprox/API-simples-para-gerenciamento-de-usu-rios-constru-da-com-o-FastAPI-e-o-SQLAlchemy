API de Gerenciamento de Usuários
API RESTful construída com FastAPI, SQLAlchemy e SQLite para gerenciamento de usuários, com operações CRUD (Criar, Ler, Atualizar, Deletar).

Descrição
Essa API permite o cadastro, listagem, atualização e remoção de usuários. Cada usuário possui informações como nome, idade e e-mail. O projeto utiliza FastAPI para criação da API, SQLAlchemy para comunicação com o banco de dados SQLite e Pydantic para validação de dados.

Funcionalidades
Cadastro de Usuário (POST /usuarios/)

Listagem de Usuários (GET /usuarios/)

Atualização de Usuário (PUT /usuarios/{usuario_id})

Exclusão de Usuário (DELETE /usuarios/{usuario_id})

Tecnologias Utilizadas
FastAPI: Framework para construção da API.

SQLAlchemy: ORM para interação com o banco de dados.

SQLite: Banco de dados relacional utilizado.

Pydantic: Validação de dados de entrada e saída.

Como Rodar o Projeto Localmente
Requisitos
Python 3.7 ou superior

pip (gerenciador de pacotes Python)

Passo a Passo
Clonar o repositório

bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Instalar as dependências

bash
Copiar
Editar
pip install -r requirements.txt
Criar o banco de dados

bash
Copiar
Editar
python -c "from database import init_db; init_db()"
Rodar a aplicação

bash
Copiar
Editar
uvicorn main:app --reload
A aplicação estará disponível em http://localhost:8000.

Endpoints
1. Criar Usuário
Método: POST
URL: /usuarios/
Corpo da Requisição:

json
Copiar
Editar
{
  "nome": "João Silva",
  "idade": 30,
  "email": "joao.silva@example.com"
}
Resposta:

json
Copiar
Editar
{
  "mensagem": "Usuário João Silva criado com sucesso id:uuid-123"
}
2. Listar Usuários
Método: GET
URL: /usuarios/

Resposta:

json
Copiar
Editar
{
  "usuarios": [
    {
      "id": "uuid-123",
      "nome": "João Silva",
      "idade": 30,
      "email": "joao.silva@example.com"
    },
    ...
  ]
}
3. Atualizar Usuário
Método: PUT
URL: /usuarios/{usuario_id}
Corpo da Requisição:

json
Copiar
Editar
{
  "nome": "João Silva Atualizado",
  "idade": 31,
  "email": "joao.silva.updated@example.com"
}
Resposta:

json
Copiar
Editar
{
  "mensagem": "Usuário uuid-123 atualizado com sucesso"
}
4. Excluir Usuário
Método: DELETE
URL: /usuarios/{usuario_id}

Resposta:

json
Copiar
Editar
{
  "mensagem": "Usuário uuid-123 excluído com sucesso!"
}
Estrutura de Diretórios
bash
Copiar
Editar
.
├── database.py        # Configuração do banco de dados
├── main.py            # Arquivo principal da aplicação FastAPI
├── models.py          # Definição do modelo do banco de dados
├── requirements.txt   # Dependências do projeto
└── README.md          # Esse arquivo
