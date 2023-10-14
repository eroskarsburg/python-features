class Employee:
    def __init__(self, nome="", cpf="", salario=0, departamento=""):
        self.Nome = nome
        self.CPF = cpf
        self.Salario = salario
        self.Departamento = departamento

    def bonificar(self):
        self.Salario = self.Salario + (self.Salario * 0.1)

class Manager(Employee):
    def __init__(self, nome="", cpf="", salario=0, departamento="", senha="", numeroFuncionarios=0):
        super().__init__(nome, cpf, salario, departamento)
        self.Senha = senha
        self.NumeroFuncionariosGerenciados = numeroFuncionarios

    def bonificar(self):
        self.Salario = self.Salario + (self.Salario * 0.15)

    def autenticar_senha(self, senha):
        return senha == self.Senha

class Seller(Employee):
    def __init__(self, nome="", cpf="", salario=0, departamento="", quantidade_vendas=0, comissao=0):
        super().__init__(nome, cpf, salario, departamento)
        self.QuantidadeVendas = quantidade_vendas
        self.Comissao = comissao

    def atualizar_quantidade_vendas(self, quantidade):
        self.QuantidadeVendas += quantidade

    def calcular_salario(self):
        self.Salario += (self.QuantidadeVendas * self.Comissao)

emp = Employee()
seller = Seller()
man = Manager()

opt = 0
while opt != 9:
    print("##### MENU #####\n- Escolha uma opção abaixo\n")
    print("1 > Cadastrar funcionário")
    print("2 > Cadastrar vendedor")
    print("3 > Cadastrar gerente")
    print("4 > Bonificar funcionário")
    print("5 > Bonificar gerente")
    print("6 > Autenticar Senha do Gerente")
    print("7 > Atualizar quantidade vendas")
    print("8 > Calcular salário vendedor")
    print("9 > Sair")

    opt = int(input())

    if opt == 1:
        print("Cadastrando funcionario:\n")
        nome = input("Nome:")
        CPF = input("CPF:")
        salario = float(input("Salario:"))
        departamento = input("Departamento:")

        emp = Employee(nome, CPF, salario, departamento)

        print("Funcionario cadastrado!")

    elif opt == 2:
        print("Cadastrando vendedor:\n")
        nome = input("Nome:")
        CPF = input("CPF:")
        salario = float(input("Salario:"))
        departamento = input("Departamento:")
        quantidadeVendas = int(input("Quantidade de vendas:"))
        comissao = int(input("Comissão:"))

        seller = Seller(nome, CPF, salario, departamento, quantidadeVendas, comissao)

        print("Vendedor cadastrado!")

    elif opt == 3:
        print("Cadastrando gerente:\n")
        nome = input("Nome:")
        CPF = input("CPF:")
        salario = float(input("Salario:"))
        departamento = input("Departamento:")
        senha = input("Senha:")
        numeroFuncionariosGerenciados = int(input("Numero de funcionarios gerenciados:"))

        man = Manager(nome, CPF, salario, departamento, senha, numeroFuncionariosGerenciados)

        print("Gerente cadastrado!")

    elif opt == 4:
        print(f"-----\nSalário: {emp.Salario}\n")
        emp.bonificar()
        print(f"Salário atualizado: {emp.Salario}\n-----")

    elif opt == 5:
        print(f"-----\nSalário: {man.Salario}\n")
        man.bonificar()
        print(f"Salário atualizado: {man.Salario}\n-----")

    elif opt == 6:
        print("-----\nDigite a senha: ")
        senha = input()
        if man.autenticar_senha(senha):
            print("-----\nSenha digitada está correta!")
            print(f"Senha: {man.Senha}")
        else:
            print("-----\nSenha incorreta! Retornando...\n-----")

    elif opt == 7:
        print("-----\nInsira a quantidade de vendas a atualizar: ")
        qntdVendas = int(input())
        print(f"Quantidade de vendas: {seller.QuantidadeVendas}")
        seller.atualizar_quantidade_vendas(qntdVendas)
        print(f"Quantidade de vendas atualizada: {seller.QuantidadeVendas}\n-----")

    elif opt == 8:
        print(f"-----\nAtual salário do vendedor: {seller.Salario}")
        seller.calcular_salario()
        print(f"Quantidade de vendas atual: {seller.QuantidadeVendas}")
        print(f"Salário do vendedor somando as comissões por venda (R${seller.Comissao},00): {seller.Salario}")

    elif opt == 9:
        print("Saindo...")