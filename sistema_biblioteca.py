#sistema de bibliotecas

class Solicitante:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

class Biblioteca:
    def __init__(self):
        self.livros = [
            Livro("Dom Casmurro"), Livro("O Pequeno Príncipe"), Livro("Capitães da Areia"),
            Livro("1984"), Livro("A Metamorfose"), Livro("O Cortiço"),
            Livro("Memórias Póstumas de Brás Cubas"), Livro("A Revolução dos Bichos"),
            Livro("Harry Potter"), Livro("Senhor dos Anéis")
        ]

    def exibir_livros(self):
        print("\nLivros disponíveis:")
        for i, livro in enumerate(self.livros):
            print(f"{i + 1}. {livro.titulo}")

    def emprestar_livro(self, solicitante, indice):
        livro = self.livros[indice - 1]
        print(f"\n{solicitante.nome} escolheu o livro: {livro.titulo}")


class SistemaBiblioteca:
    def iniciar(self):
        biblioteca = Biblioteca()
        nome = input("Digite o nome do solicitante: ")
        solicitante = Solicitante(nome)
        biblioteca.exibir_livros()
        escolha = int(input("Escolha o livro (número): "))
        biblioteca.emprestar_livro(solicitante, escolha)


SistemaBiblioteca().iniciar()