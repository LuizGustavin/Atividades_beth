class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Fruta:
    def __init__(self, nome):
        self.nome = nome

class Feira:
    def __init__(self):
        self.frutas = [Fruta(nome) for nome in ["Maçã", "Banana", "Laranja", "Uva", "Melancia", "Manga", "Abacaxi", "Morango"]]

    def exibir_frutas(self):
        print("\nFrutas disponíveis:\n")
        for i, fruta in enumerate(self.frutas):
            print(f"{i + 1}. {fruta.nome}")

    def selecionar_fruta(self, cliente, indice):
        fruta = self.frutas[indice - 1]
        print(f"\n{cliente.nome}, você escolheu a fruta: {fruta.nome}\n")


class SistemaFeira:
    def iniciar(self):
        feira = Feira()
        nome = input("Digite seu nome: ")
        cliente = Cliente(nome)
        feira.exibir_frutas()
        escolha = int(input("Escolha uma fruta (número): "))
        feira.selecionar_fruta(cliente, escolha)

SistemaFeira().iniciar()