import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sistema"
)
cursor = conexao.cursor()

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def cadastrar(self, cursor, conexao):
        cursor.execute("SELECT * FROM Usuarios WHERE email = %s", (self.email,))
        if cursor.fetchone():
            print("Já existe um usuário com este email.")
            return
        cursor.execute("INSERT INTO Usuarios(nome, email, senha) VALUES (%s, %s, %s)", (self.nome, self.email, self.senha))
        conexao.commit()
        print(f"{self.nome} cadastrado(a) com sucesso.")

    def login(self, cursor):
        cursor.execute("SELECT nome FROM Usuarios WHERE email = %s AND senha = %s", (self.email, self.senha))
        resultado = cursor.fetchone()
        if resultado:
            print(f"Bem-vindo(a), {resultado[0]}.")
        else:
            print("Email ou senha incorretos.")

while True:
    print("\n ==== MENU ====")
    print("1 - Cadastrar Usuario")
    print("2 - Fazer login")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha (8 números): ")
        usuario = Usuario(nome, email, senha)
        usuario.cadastrar(cursor, conexao)

    elif opcao == "2":
        email = input("Email: ")
        senha = input("Senha: ")
        usuario = Usuario(" ", email, senha)
        usuario.login(cursor)

    elif opcao == "3":
        cursor.close()
        conexao.close()
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")