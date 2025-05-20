import sqlite3

conn = sqlite3.connect('crud_usuarios.bd')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
''')
conn.commit

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite sua idade: "))
    cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?,?)', (nome, idade))
    conn.commit()
    print(f"Usuário {nome} criado com sucesso!!")

def listar_usuario():
    cursor.execute ('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    if not usuarios:
        print("Nenhum usuário cadastrado")
    else:
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Idade: {usuario[2]}")

def buscar_usuario():
    id = int(input("Digite o ID do usuário: "))
    cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
    usuario = cursor.fetchone()
    if usuario:
        print(f"ID {usuario[0]}, Nome {usuario[1]}, Idade {usuario[2]}")

def atualizar_usuario():
    id = int(input("Digite o ID de usuário que deseja atualizar: "))
    cursor.execute ('SELECT * FROM usuarios WHERE id = ?', (id,))
    usuario = cursor.fetchone()
    if usuario:
        nome = input(f"Digite o novo nome: ")
        idade = input(f"Digite a nova idade: ")
        if nome:
            cursor.execute('UPDATE usuarios SET nome = ? WHERE id = ?', (nome, id))
        if idade:
            cursor.execute('UPDATE usuarios SET idade = ? WHERE id = ?', (int(idade), id))
        conn.commit()
        print(f"Usuário ID: {id} atualizado com sucesso")
    else:
        print("Usuário não encontrado")

def deletar_usuario():
    id= int(input("Digite o numero de ID que deseja excluir: "))
    cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
    usario = cursor.fetchone()
    if usario:
        cursor.execute('DELETE FROM usuarios WHERE id= ?', (id,))
        conn.commit()
        print(f"Usuário ID {id} deletado com sucesso!")
    else:
        print("Usuário não encontrado")


def menu():
    while True:
        print("\n--- CRUD de Usuários ---")
        print("1. Criar usuário")
        print("2. Listar usuário")
        print("3. Buscar usuário por ID")
        print("4. Atualizar usuário")
        print("5. Deletar usuário")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            listar_usuario()
        elif opcao == "3":
            buscar_usuario()
        elif opcao == "4":
            atualizar_usuario()
        elif opcao == "5":
            deletar_usuario()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()

conn.close()
