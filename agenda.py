class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome} - {self.telefone}"

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        self.contatos.append(Contato(nome, telefone))

    def listar_contatos(self):
        print("\n=== Contatos na Agenda ===\n")
        for contato in self.contatos:
            print(contato)


agenda = Agenda()
agenda.adicionar_contato("Ana", "9999-0001")
agenda.adicionar_contato("Carlos", "9888-1234")



agenda.listar_contatos()