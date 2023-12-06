# Sistema de Gerenciamento de Pedidos - Projeto Inicial

Este repositório é um projeto inicial para um sistema de gerenciamento de pedidos em Django. Até o momento, a estrutura do projeto foi definida, mas ainda não foram implementadas funcionalidades específicas.

## Como Iniciar o Projeto

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
```

## Dependências
```
asgiref==3.7.2
Django==5.0
prettytable==3.9.0
python-dotenv==1.0.0
sqlparse==0.4.4
typing_extensions==4.8.0
wcwidth==0.2.12
```
## Contribuições e Sugestões de Melhoria

Contribuições e sugestões de melhoria são bem-vindas! Se encontrar algum problema, tiver ideias para novos recursos ou melhorias, sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**

Estamos ansiosos para tornar este projeto ainda melhor com a ajuda da comunidade!
