class Empregado:
    def __init__(self, nome):
        self.Nome = nome
    def retornaPagamento(self):
        pass

class Assalariado(Empregado):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.Salario = salario
    def retornaPagamento(self):
        return self.Salario

class Horista(Empregado):
    def __init__(self, nome, valorHora, qntHoras):
        super().__init__(nome)
        self.ValorHora = valorHora
        self.QuantidadeHoras = qntHoras
    def retornaPagamento(self):
        return (self.ValorHora * self.QuantidadeHoras * 4.5)

class Menu:
    def empregadoSelection(self):
        print("Selecione o Empregado:\n"
              "1. Assalariado\n"
              "2. Horista\n"
              "-----------\n"
              "3. Mostrar folha de pagamento")
    def menuHorista(self):
        print("Selecionado: Horista\n")
        nome = input("Insira o nome: ")
        valorHora = float(input("Insira o valor da Hora: "))
        qntHoras = int(input("Insira a quantidade de horas trabalhadas: "))
        return Horista(nome, valorHora, qntHoras)

    def menuAssalariado(self):
        print("Selecionado: Assalariado\n")
        nome = input("Insira o nome: ")
        salario = float(input("Insira o salário: "))
        return Assalariado(nome, salario)


## MAIN
menu = Menu()
option = -1
empregados = []
folhaPagamento = 0

while option != 3:
    try:
        menu.empregadoSelection()
        option = int(input("> "))
        if option == 1:
            empregado = menu.menuAssalariado()
        if option == 2:
            empregado = menu.menuHorista()
        if option == 3:
            print("\nResumo da folha de pagamento:")
            for empregado in empregados:
                print(f'    {empregado.Nome}: {empregado.retornaPagamento()}')
            print(f"\nGasto total com a folha salarial: R${folhaPagamento}")
            continue

        empregados.append(empregado)
        folhaPagamento += empregado.retornaPagamento()
    except ValueError as e:
        print("Valor incorreto. Tente novamente.")
