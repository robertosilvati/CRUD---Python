import sqlite3
from prettytable import PrettyTable

def formatarComoMoeda(valor):
    return f'R$ {valor:.2f}'

def create_tables():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pedido_id INTEGER,
            produto TEXT,
            valor REAL,
            quantidade INTEGER,
            valor_final REAL,
            FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
        )
    ''')
    connection.commit()
    connection.close()

def insert_pedido():
    try:
        cliente = input("Nome do cliente: ")

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO pedidos (cliente)
            VALUES (?)
        ''', (cliente,))
        pedido_id = cursor.lastrowid
        connection.commit()
        connection.close()
        
        print(f"Pedido {pedido_id} inserido com sucesso.")
        return pedido_id
    except ValueError:
        print("Erro ao inserir pedido. Certifique-se de fornecer valores válidos.")
        return None

def insert_produto(pedido_id):
    while True:
        try:
            produto = input("Produto: ")
            valor = float(input("Valor do produto: "))
            quantidade = int(input("Quantidade: "))
            
            if valor < 0 or quantidade < 0:
                print("Valor e quantidade devem ser números positivos.")
                return

            valor_final = valor * quantidade

            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO produtos (pedido_id, produto, valor, quantidade, valor_final)
                VALUES (?, ?, ?, ?, ?)
            ''', (pedido_id, produto, valor, quantidade, valor_final))
            connection.commit()
            connection.close()
            print("Produto adicionado ao pedido com sucesso.")

            continuar = input("Deseja adicionar mais um produto? (S/N): ").upper()
            if continuar != 'S':
                break
        except ValueError:
            print("Erro ao inserir produto. Certifique-se de fornecer valores válidos.")
            break

def get_all_records():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''
        SELECT pedidos.id, pedidos.cliente, produtos.id, produtos.produto, produtos.valor, produtos.quantidade, produtos.valor_final, pedidos.data_hora
        FROM pedidos
        LEFT JOIN produtos ON pedidos.id = produtos.pedido_id
        ORDER BY pedidos.id, produtos.id
    ''')
    rows = cursor.fetchall()
    connection.close()
    return rows

def display_records(records):
    table = PrettyTable()
    table.field_names = ["ID Pedido", "Cliente", "ID Produto", "Produto", "Valor", "Quantidade", "Valor Final", "Data e Hora"]
    current_pedido_id = None

    for record in records:
        if current_pedido_id is None or record[0] != current_pedido_id:
            table.add_row([record[0], record[1], "", "", "", "", "", record[7]])
            current_pedido_id = record[0]

        table.add_row(["", "", record[2], record[3], formatarComoMoeda(record[4]), record[5], formatarComoMoeda(record[6]), ""])

    print(table)

def update_record():
    try:
        records = get_all_records()
        display_records(records)

        id_pedido = int(input("\nDigite o ID do pedido que deseja atualizar: "))

        if not any(record[0] == id_pedido for record in records):
            print("Pedido não encontrado.")
            return

        print("O que deseja atualizar neste pedido?")
        print("1 - Nome do Cliente")
        print("2 - Produtos")
        escolha = input("Digite o número da opção desejada: ")

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        if escolha == '1':
            novo_cliente = input("Digite o novo nome do cliente: ")
            confirmacao = input(f"Tem certeza de que deseja alterar o nome do cliente para '{novo_cliente}'? (S/N): ").upper()

            if confirmacao == 'S':
                cursor.execute('UPDATE pedidos SET cliente=? WHERE id=?', (novo_cliente, id_pedido))
                connection.commit()
                print("Nome do cliente atualizado com sucesso.")
            else:
                print("Operação cancelada.")
        elif escolha == '2':
            while True:
                print("O que deseja fazer com os produtos?")
                print("1 - Adicionar novo produto")
                print("2 - Editar produto existente")
                print("3 - Excluir produto")
                print("0 - Sair")
                escolha_produto = input("Digite o número da opção desejada: ")

                if escolha_produto == '1':
                    produto = input("Produto: ")
                    valor = float(input("Valor do produto: "))
                    quantidade = int(input("Quantidade: "))
                    
                    if valor < 0 or quantidade < 0:
                        print("Valor e quantidade devem ser números positivos.")
                        continue

                    valor_final = valor * quantidade

                    cursor.execute('''
                        INSERT INTO produtos (pedido_id, produto, valor, quantidade, valor_final)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (id_pedido, produto, valor, quantidade, valor_final))
                    connection.commit()
                    print("Produto adicionado ao pedido com sucesso.")
                elif escolha_produto == '2':
                    produto_id = int(input("Digite o ID do produto que deseja editar (0 para sair): "))

                    if produto_id == 0:
                        break
                    if not any(record[2] == produto_id and record[0] == id_pedido for record in records):
                        print("Produto não encontrado no pedido.")
                        continue

                    produto = input("Atualizar dados do produto: ")
                    valor = float(input("Atualizar valor do produto: "))
                    quantidade = int(input("Atualizar a quantidade: "))

                    if valor < 0 or quantidade < 0:
                        print("Valor e quantidade devem ser números positivos.")
                        continue

                    valor_final = valor * quantidade

                    cursor.execute('''
                        UPDATE produtos 
                        SET produto=?, valor=?, quantidade=?, valor_final=?
                        WHERE pedido_id=? AND id=?
                    ''', (produto, valor, quantidade, valor_final, id_pedido, produto_id))
                    connection.commit()
                    print("Produto atualizado com sucesso.")
                elif escolha_produto == '3':
                    produto_id = int(input("Digite o ID do produto que deseja excluir (0 para sair): "))

                    if produto_id == 0:
                        break
                    if not any(record[2] == produto_id and record[0] == id_pedido for record in records):
                        print("Produto não encontrado no pedido.")
                        continue

                    cursor.execute('DELETE FROM produtos WHERE pedido_id=? AND id=?', (id_pedido, produto_id))
                    connection.commit()
                    print("Produto excluído do pedido com sucesso.")
                elif escolha_produto == '0':
                    break
                else:
                    print("Opção inválida.")
        else:
            print("Opção inválida. Nada foi atualizado.")

        connection.close()
    except ValueError:
        print("Erro ao atualizar pedido. Certifique-se de fornecer valores válidos.")

def delete_record():
    try:
        records = get_all_records()
        display_records(records)

        id_pedido = int(input("\nDigite o ID do pedido para ser excluido: "))

        if not any(record[0] == id_pedido for record in records):
            print("Pedido não encontrado.")
            return

        print("\nInformações do pedido a ser excluído:")
        pedido_a_excluir = [record for record in records if record[0] == id_pedido]
        if pedido_a_excluir:
            display_records(pedido_a_excluir)
        else:
            print("Pedido não encontrado.")
            return

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM produtos WHERE pedido_id=?', (id_pedido,))
        cursor.execute('DELETE FROM pedidos WHERE id=?', (id_pedido,))
        connection.commit()
        connection.close()

        print(f"Pedido {id_pedido} e seus produtos associados foram excluídos com sucesso.")
    except ValueError:
        print("Erro ao excluir pedido. Certifique-se de fornecer um ID de pedido válido.")

create_tables()

while True:
    print("""
    ================================
            Projetinho CRUD
    ================================
    1 - Inserir um novo pedido
    2 - Visualizar todos os pedidos
    3 - Atualizar um pedido
    4 - Excluir um pedido
    0 - Sair
    ================================
    """)

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        pedido_id = insert_pedido()
        if pedido_id is not None:
            insert_produto(pedido_id)
    elif escolha == '2':
        records = get_all_records()
        display_records(records)
    elif escolha == '3':
        update_record()
    elif escolha == '4':
        delete_record()
    elif escolha == '0':
        break
    else:
        print("Opção inválida. Tente novamente.")