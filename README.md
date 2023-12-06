# Sistema de Gerenciamento de Pedidos - Projeto CRUD

Este repositório contém um simples sistema de gerenciamento de pedidos desenvolvido em Django, utilizando SQLite como banco de dados. O projeto é um exemplo de CRUD (Create, Read, Update, Delete) que permite:

- **Inserir um Novo Pedido:** Adicione informações sobre o cliente e produtos associados.
- **Visualizar Todos os Pedidos:** Consulte uma lista completa de pedidos, incluindo detalhes dos produtos.
- **Atualizar um Pedido:** Modifique o nome do cliente ou ajuste os detalhes dos produtos existentes.
- **Excluir um Pedido:** Remova pedidos e seus produtos associados do sistema.

## Como Usar

1. **Clone este repositório:**
    ```bash
    git clone https://github.com/robertosilvati/setup.git
    cd setup
    ```

2. **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    # Ou
    .\venv\Scripts\activate  # Para Windows
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Execute o servidor Django:**
    ```bash
    python manage.py runserver
    ```

5. **Acesse a aplicação em [http://localhost:8000/](http://localhost:8000/)**

## Estrutura do Projeto

```plaintext
setup/
|-- setup/
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   |-- wsgi.py
|-- crud/
|   |-- migrations/
|   |-- templates/
|   |-- static/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- views.py
|-- manage.py
|-- requirements.txt
|-- README.md

##  Dependências
asgiref==3.7.2
Django==5.0
prettytable==3.9.0
python-dotenv==1.0.0
sqlparse==0.4.4
typing_extensions==4.8.0
wcwidth==0.2.12