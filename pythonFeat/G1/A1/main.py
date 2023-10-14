class Pessoa:
    def __init__(self, nome, idade, sexo, endereco):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def setIdade(self, sexo):
        self.sexo = sexo

    def setIdade(self, endereco):
        self.endereco = endereco


def showData():
    p1 = Pessoa('Eros', 20, "M", "R. Gen Neto")
    p2 = Pessoa('Adanarys', 20, "F", "R. Mathias Velho")
    p3 = Pessoa('Gabriel', 20, "M", "Centro")
    p4 = Pessoa('Julia', 20, "F", "R. Guarulhos")

    print(p1.nome, p1.idade, p1.sexo, p1.endereco + "\n")
    print(p2.nome, p2.idade, p2.sexo, p2.endereco + "\n")
    print(p3.nome, p3.idade, p3.sexo, p3.endereco + "\n")
    print(p4.nome, p4.idade, p4.sexo, p4.endereco + "\n")

showData()