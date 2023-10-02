class Montadora:
    def __init__(self, codigo, estado, razao_social):
        self.codigo = codigo
        self.estado = estado
        self.razao_social = razao_social

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_codigo(self):
        return self.codigo

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_razao_social(self, razao_social):
        self.razao_social = razao_social

    def get_razao_social(self):
        return self.razao_social


class Modelo:
    def __init__(self, codigo, nome, montadora):
        self.codigo = codigo
        self.nome = nome
        self.montadora = montadora

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_codigo(self):
        return self.codigo

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_montadora(self, montadora):
        self.montadora = montadora

    def get_montadora(self):
        return self.montadora


class Carro:
    def __init__(self, placa, modelo, ano_fabricacao):
        self.placa = placa
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao

    def set_placa(self, placa):
        self.placa = placa

    def get_placa(self):
        return self.placa

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo

    def set_ano_fabricacao(self, ano_fabricacao):
        self.ano_fabricacao = ano_fabricacao

    def get_ano_fabricacao(self):
        return self.ano_fabricacao


# Função para criar uma instância da classe Montadora a partir dos dados fornecidos pelo usuário
def criar_montadora():
    codigo = int(input("Digite o código da montadora: "))
    estado = input("Digite o estado da montadora (2 caracteres): ")
    razao_social = input("Digite a razão social da montadora: ")
    return Montadora(codigo, estado, razao_social)


# Função para criar uma instância da classe Modelo a partir dos dados fornecidos pelo usuário
def criar_modelo(montadora):
    codigo = int(input("Digite o código do modelo: "))
    nome = input("Digite o nome do modelo: ")
    return Modelo(codigo, nome, montadora)


# Função para criar uma instância da classe Carro a partir dos dados fornecidos pelo usuário
def criar_carro(modelo):
    placa = input("Digite a placa do carro: ")
    ano_fabricacao = int(input("Digite o ano de fabricação do carro: "))
    return Carro(placa, modelo, ano_fabricacao)


# Função para exibir os dados de uma instância de Montadora
def exibir_montadora(montadora):
    print(f"Código da Montadora: {montadora.get_codigo()}")
    print(f"Estado da Montadora: {montadora.get_estado()}")
    print(f"Razão Social da Montadora: {montadora.get_razao_social()}")


# Função para exibir os dados de uma instância de Modelo
def exibir_modelo(modelo):
    print(f"Código do Modelo: {modelo.get_codigo()}")
    print(f"Nome do Modelo: {modelo.get_nome()}")
    print("Montadora do Modelo:")
    exibir_montadora(modelo.get_montadora())


# Função para exibir os dados de uma instância de Carro
def exibir_carro(carro):
    print(f"Placa do Carro: {carro.get_placa()}")
    print("Dados do Modelo do Carro:")
    exibir_modelo(carro.get_modelo())
    print(f"Ano de Fabricação do Carro: {carro.get_ano_fabricacao()}")


# Função para permitir ao usuário alterar os atributos de uma instância de Montadora
def alterar_montadora(montadora):
    print("Selecione o atributo que deseja alterar:")
    print("1. Código da Montadora")
    print("2. Estado da Montadora")
    print("3. Razão Social da Montadora")
    opcao = int(input("Digite o número da opção: "))
    if opcao == 1:
        novo_codigo = int(input("Digite o novo código da montadora: "))
        montadora.set_codigo(novo_codigo)
    elif opcao == 2:
        novo_estado = input("Digite o novo estado da montadora (2 caracteres): ")
        montadora.set_estado(novo_estado)
    elif opcao == 3:
        nova_razao_social = input("Digite a nova razão social da montadora: ")
        montadora.set_razao_social(nova_razao_social)
    else:
        print("Opção inválida")


# Função para permitir ao usuário alterar os atributos de uma instância de Modelo
def alterar_modelo(modelo):
    print("Selecione o atributo que deseja alterar:")
    print("1. Código do Modelo")
    print("2. Nome do Modelo")
    opcao = int(input("Digite o número da opção: "))
    if opcao == 1:
        novo_codigo = int(input("Digite o novo código do modelo: "))
        modelo.set_codigo(novo_codigo)
    elif opcao == 2:
        novo_nome = input("Digite o novo nome do modelo: ")
        modelo.set_nome(novo_nome)
    else:
        print("Opção inválida")


# Função para permitir ao usuário alterar os atributos de uma instância de Carro
def alterar_carro(carro):
    print("Selecione o atributo que deseja alterar:")
    print("1. Placa do Carro")
    print("2. Modelo do Carro")
    print("3. Ano de Fabricação do Carro")
    opcao = int(input("Digite o número da opção: "))
    if opcao == 1:
        nova_placa = input("Digite a nova placa do carro: ")
        carro.set_placa(nova_placa)
    elif opcao == 2:
        print("Dados atuais do Modelo do Carro:")
        exibir_modelo(carro.get_modelo())
        novo_modelo = criar_modelo()
        carro.set_modelo(novo_modelo)
    elif opcao == 3:
        novo_ano_fabricacao = int(input("Digite o novo ano de fabricação do carro: "))
        carro.set_ano_fabricacao(novo_ano_fabricacao)
    else:
        print("Opção inválida")

        # Função principal
def main():
    # Criação das instâncias das classes
    montadora = criar_montadora()
    modelo = criar_modelo(montadora)
    carro = criar_carro(modelo)

    while True:
        print("\nMenu:")
        print("1. Exibir dados das instâncias")
        print("2. Alterar atributos das instâncias")
        print("3. Sair")
        opcao_menu = int(input("Digite o número da opção: "))

        if opcao_menu == 1:
            print("\nDados da Montadora:")
            exibir_montadora(montadora)
            print("\nDados do Modelo:")
            exibir_modelo(modelo)
            print("\nDados do Carro:")
            exibir_carro(carro)
        elif opcao_menu == 2:
            print("Selecione a instância que deseja alterar:")
            print("1. Montadora")
            print("2. Modelo")
            print("3. Carro")
            opcao_instancia = int(input("Digite o número da opção: "))
            if opcao_instancia == 1:
                alterar_montadora(montadora)
            elif opcao_instancia == 2:
                alterar_modelo(modelo)
            elif opcao_instancia == 3:
                alterar_carro(carro)
            else:
                print("Opção inválida")
        elif opcao_menu == 3:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()