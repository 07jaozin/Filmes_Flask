# Filmes_Flask
🎬 Site de Gerenciamento de Filmes

Este é um sistema completo de gerenciamento de filmes desenvolvido em Flask, com suporte a MySQL.
O site oferece uma experiência intuitiva para usuários e administradores, com funcionalidades de cadastro,
visualização, edição e exclusão de filmes.

🚀 Funcionalidades

👤 Usuário:
- Cadastro e Login: Criação de conta com autenticação segura.
- Home: Lista de filmes com opção de detalhes.
- Perfil do Filme:
  - Visualização completa das informações do filme.
  - Ver Trailer diretamente no navegador.
  - Baixar Trailer como arquivo.
- Perfil do Usuário:
  - Edição de nome, senha e foto de perfil.
  - Opção para excluir a conta.
- Pesquisa de Filmes: Busca por nome.
- Logout: Encerra a sessão com segurança.

🔧 Administrador:
- Adicionar Filmes: Cadastro de novos títulos.
- Tabela de Filmes: Visualização geral com opções de:
  - Editar: Alterar dados de um filme.
  - Excluir: Remover um filme do sistema.

📁 Estrutura do Projeto

/dao         → Conexão com MySQL e execução de SQL com Python  
/controller  → Validação e segurança dos dados  
/model       → Definição das classes, métodos e rotas dos filmes  
/static      → Arquivos estáticos: JS, CSS, imagens, vídeos  
/templates   → Templates HTML  
/config      → Configurações do sistema e variáveis de ambiente  
app.py       → Arquivo principal que gerencia as rotas e requisições  

⚡ Como Usar

1. Clone o repositório:
   git clone https://github.com/07jaozin/seu-projeto.git
   cd seu-projeto

2. Crie um ambiente virtual e instale as dependências:
   python -m venv venv
   source venv/bin/activate     (Windows: venv\\Scripts\\activate)
   pip install flask
   pip install mysql-connector-python
   pip install -r requirements.txt

3. Configure o banco de dados MySQL e edite as credenciais na pasta /dao.
CREATE DATABASE if not exists filmes;

use filmes;

create table if not exists filme(
	id INT auto_increment primary key,
    titulo VARCHAR(255) NOT NULL,
    genero varchar(255) NOT NULL, 
    categoria varchar(255) NOT NULL,
    lancamento varchar(255) NOT NULL, 
    foto varchar(255) NOT NULL, 
    video varchar(255) NOT NULL
    
); 

Usuarios:
CREATE DATABASE if not exists usuarios;

use usuarios;

create table if not exists usuario(
	id INT auto_increment primary key,
    nome VARCHAR(255) NOT NULL,
	senha VARCHAR(255) NOT NULL,
	foto VARCHAR(255) NOT NULL
    

);
4. Execute o sistema:
   dentro de projeto:
   set FLASK_APP=app.py (Windows) ou export FLASK_APP=app.py (Linux)

    flask run
    
📌 Requisitos

- Python 3.x  
- Flask  
- MySQL  

👨‍💻 Autor

Desenvolvido por João Victor Valentim de Oliveira  
GitHub: https://github.com/07jaozin
