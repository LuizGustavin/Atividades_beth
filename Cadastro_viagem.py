

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

class Aluno(Pessoa):
    pass

class Professor(Pessoa):
    pass

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = set()
        self.professores = set()

    def adicionar_aluno(self, aluno):
        self.alunos.add(aluno)

    def adicionar_professor(self, professor):
        self.professores.add(professor)

    def listar_participantes(self):
        print(f"\nCurso: {self.nome}")
        print("Professores:")
        for prof in self.professores:
            print(f" - {prof}")
        print("Alunos:")
        for aluno in self.alunos:
            print(f" - {aluno}")


curso = Curso("Python Básico")
curso.adicionar_aluno(Aluno("João"))
curso.adicionar_aluno(Aluno("Maria"))
curso.adicionar_professor(Professor("Prof. Carlos"))
curso.listar_participantes()
