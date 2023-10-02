class Montadora:
    def __init__(self, codigo_montadora=None, estado=None, razao_social=None):
        self.CodigoMontadora = codigo_montadora
        self.Estado = estado
        self.RazaoSocial = razao_social

    def __str__(self):
        return f"-> Montadora:\nCódigo: {self.CodigoMontadora},\nEstado: {self.Estado},\nRazão Social: {self.RazaoSocial}"


class Modelo:
    def __init__(self, codigo_modelo=None, nome_modelo=None, montadora=None):
        self.CodigoModelo = codigo_modelo
        self.NomeModelo = nome_modelo
        self.Montadora = montadora

    def __str__(self):
        if self.Montadora is not None:
            return f"-> Modelo:\nCódigo: {self.CodigoModelo},\nNome: {self.NomeModelo}," \
                   f"\n    Código Montadora: {self.Montadora.CodigoMontadora}," \
                   f"\n    Razão Social Montadora: {self.Montadora.RazaoSocial}," \
                   f"\n    Estado Montadora: {self.Montadora.Estado}"
        else:
            return f"-> Modelo:\nCódigo: {self.CodigoModelo},\nNome: {self.NomeModelo},\n    Montadora: None"


class Carro:
    def __init__(self, placa=None, modelo=None, ano_fabricacao=None):
        self.Placa = placa
        self.Modelo = modelo
        self.AnoFabricacao = ano_fabricacao

    def __str__(self):
        return f"-> Carro:\nPlaca: {self.Placa},\n    Código Modelo: {self.Modelo.CodigoModelo}," \
               f"\n    Nome Modelo: {self.Modelo.NomeModelo}," \
               f"\n        Código Montadora: {self.Modelo.Montadora.CodigoMontadora}," \
               f"\n        Razão Social Montadora: {self.Modelo.Montadora.RazaoSocial}," \
               f"\n        Estado Montadora: {self.Modelo.Montadora.Estado}," \
               f"\nAno fabricação: {self.AnoFabricacao}"


class Menus:
    def MenuAutomovel(self):
        print("#### Menu ####")
        print("1. Cadastrar Automóvel: ")
        print("--------------")
        print("2. Mostrar Automóvel cadastrado: ")
        print("--------------")
        print("3. Atualizar valor cadastrado: ")
        print("--------------")
        print("4. Sair: ")

    def MenuCadastrarAutomovel(self):
        print("1. Cadastrar Montadora: ")
        print("2. Cadastrar Modelo: ")
        print("3. Cadastrar Carro: ")
        print("4. Voltar: ")

    def MenuAtualizarAutomovel(self):
        print("-> Escolha o que será atualizado ")
        print("--------------")
        print("1. Atualizar Montadora: ")
        print("2. Atualizar Modelo: ")
        print("3. Atualizar Carro: ")
        print("4. Voltar: ")

    def MenuAtualizarMontadora(self):
        print("-- Montadora --")
        print("-> Qual atributo será alterado?")
        print("1. Código")
        print("2. Estado")
        print("3. Razão Social")

    def MenuAtualizarModelo(self):
        print("-- Modelo --")
        print("-> Qual atributo será alterado?")
        print("1. Código")
        print("2. Nome")

    def MenuAtualizarCarro(self):
        print("-- Carro --")
        print("-> Qual atributo será alterado?")
        print("1. Placa")
        print("2. Ano de fabricação")


class AutomovelRepository:
    def __init__(self):
        self.listaMontadora = []
        self.listaModelo = []
        self.listaCarro = []

    def MostrarAtributosAutomovel(self):
        for montadora in self.listaMontadora:
            print("\n" + str(montadora))
        for modelo in self.listaModelo:
            print("\n" + str(modelo))
        for carro in self.listaCarro:
            print("\n" + str(carro) + "\n")

    def CadastrarMontadora(self):
        try:
            print("### Montadora ###")
            codigo_montadora = int(input("-> Codigo: "))
            razao_social = input("-> Razão Social: ")
            estado = input("-> Estado: ")
            
            montadora = Montadora(codigo_montadora, estado, razao_social)
            self.listaMontadora.append(montadora)
            
            print("\nCadastro finalizado!\n")
        except Exception as ex:
            print(f"Ocorreu um erro.\nErro: {ex}")

    def CadastrarModelo(self):
        try:
            if not self.listaMontadora:
                print("\nNão há nenhuma montadora cadastrada para fazer vínculo a este modelo.\n")
                return
            
            print("### Modelo ###")
            codigo_modelo = int(input("-> Codigo: "))
            nome_modelo = input("-> Nome do Modelo: ")
            codigo_montadora = int(input("-> Código da Montadora: "))
            
            if not self.VerificarMontadoraExistente(codigo_montadora):
                print("Não há Montadora cadastrada com esse código.")
                return
            
            modelo = Modelo(codigo_modelo, nome_modelo, self.listaMontadora[-1])
            self.listaModelo.append(modelo)
            
            print("\nCadastro finalizado!\n")
        except Exception as ex:
            print(f"Ocorreu um erro.\nErro: {ex}")

    def CadastrarCarro(self):
        try:
            if not self.listaModelo:
                print("\nNão há nenhum modelo cadastrado para fazer vínculo a este carro.\n")
                return
            
            print("### Carro ###")
            placa = input("-> Placa: ")
            ano_fabricacao = int(input("-> Ano de fabricação: "))
            codigo_modelo = int(input("-> Código do Modelo: "))
            
            if not self.VerificarModeloExistente(codigo_modelo):
                print("Não há Modelo cadastrado com esse código.")
                return
            
            carro = Carro(placa, self.listaModelo[-1], ano_fabricacao)
            self.listaCarro.append(carro)
            
            print("\nCadastro finalizado!\n")
        except Exception as ex:
            print(f"Ocorreu um erro.\nErro: {ex}")

    def VerificarMontadoraExistente(self, codigo_montadora):
        for montadora in self.listaMontadora:
            if montadora.CodigoMontadora == codigo_montadora:
                return True
        return False

    def VerificarModeloExistente(self, codigo_modelo):
        for modelo in self.listaModelo:
            if modelo.CodigoModelo == codigo_modelo:
                return True
        return False

    def BuscarMontadora(self, codigo_mont):
        for montadora in self.listaMontadora:
            if montadora.CodigoMontadora == codigo_mont:
                print("\nMontadora a ser atualizada: ")
                print(montadora)
                return True
        return False

    def BuscarModelo(self, codigo_modelo):
        for modelo in self.listaModelo:
            if modelo.CodigoModelo == codigo_modelo:
                print("\nModelo a ser atualizado: ")
                print(modelo)
                return True
        return False

    def BuscarCarro(self, placa):
        for carro in self.listaCarro:
            if carro.Placa == placa:
                print("\nCarro a ser atualizado: ")
                print(carro)
                return True
        return False

    def AtualizarMontadoraCodigo(self, codigo, novo_codigo):
        for montadora in self.listaMontadora:
            if montadora.CodigoMontadora == codigo:
                montadora.CodigoMontadora = novo_codigo
                print("\nMontadora Atualizada!\n")
                return

    def AtualizarMontadoraEstado(self, codigo, novo_estado):
        for montadora in self.listaMontadora:
            if montadora.CodigoMontadora == codigo:
                montadora.Estado = novo_estado
                print("\nMontadora Atualizada!\n")
                return

    def AtualizarMontadoraRazaoSocial(self, codigo, nova_razao_social):
        for montadora in self.listaMontadora:
            if montadora.CodigoMontadora == codigo:
                montadora.RazaoSocial = nova_razao_social
                print("\nMontadora Atualizada!\n")
                return

    def AtualizarModeloCodigo(self, codigo, novo_codigo):
        for modelo in self.listaModelo:
            if modelo.CodigoModelo == codigo:
                modelo.CodigoModelo = novo_codigo
                print("\nModelo Atualizado!\n")
                return

    def AtualizarModeloNome(self, codigo, novo_nome):
        for modelo in self.listaModelo:
            if modelo.CodigoModelo == codigo:
                modelo.NomeModelo = novo_nome
                print("\nModelo Atualizado!\n")
                return

    def AtualizarCarroPlaca(self, placa, nova_placa):
        for carro in self.listaCarro:
            if carro.Placa == placa:
                carro.Placa = nova_placa
                print("\nCarro Atualizado!\n")
                return

    def AtualizarCarroAnoFabricacao(self, placa, novo_ano_fabricacao):
        for carro in self.listaCarro:
            if carro.Placa == placa:
                carro.AnoFabricacao = novo_ano_fabricacao
                print("\nCarro Atualizado!\n")
                return


# Create an instance of Automovel class
automovel = AutomovelRepository()
menu = Menus()
opt = 0

while opt != 4:
    menu.MenuAutomovel()
    opt = int(input())

    if opt == 1:
        automovel.CadastrarMontadora()
        automovel.CadastrarModelo()
        automovel.CadastrarCarro()

    if opt == 2:
        automovel.MostrarAtributosAutomovel()

    if opt == 3:
        menu.MenuAtualizarAutomovel()
        opt2 = int(input())

        if opt2 == 1:
            print("Insira o código da montadora que deseja alterar: ")
            codMont = int(input())

            if not automovel.BuscarMontadora(codMont):
                print("\nNão foi encontrado nenhuma Montadora.\n")
                break

            menu.MenuAtualizarMontadora()
            opt3 = int(input())

            if opt3 == 1:
                print("Insira o novo valor: ")
                novoCodigo = int(input())
                automovel.AtualizarMontadoraCodigo(codMont, novoCodigo)

            if opt3 == 2:
                print("Insira o novo valor: ")
                novoEstado = input()
                automovel.AtualizarMontadoraEstado(codMont, novoEstado)

            if opt3 == 3:
                print("Insira o novo valor: ")
                novaRazao = input()
                automovel.AtualizarMontadoraRazaoSocial(codMont, novaRazao)

        if opt2 == 2:
            print("Insira o código do modelo que deseja alterar: ")
            codModelo = int(input())

            if not automovel.BuscarModelo(codModelo):
                print("\nNão foi encontrado nenhum Modelo.\n")
                break

            menu.MenuAtualizarModelo()
            opt3 = int(input())

            if opt3 == 1:
                print("Insira o novo valor: ")
                novoCodigo = int(input())
                automovel.AtualizarModeloCodigo(codModelo, novoCodigo)

            if opt3 == 2:
                print("Insira o novo valor: ")
                novoNome = input()
                automovel.AtualizarModeloNome(codModelo, novoNome)

        if opt2 == 3:
            print("Insira a placa do carro que deseja alterar: ")
            placa = input()

            if not automovel.BuscarCarro(placa):
                print("\nNão foi encontrado nenhum Carro.\n")
                break

            menu.MenuAtualizarCarro()
            opt3 = int(input())

            if opt3 == 1:
                print("Insira o novo valor: ")
                novaPlaca = input()
                automovel.AtualizarCarroPlaca(placa, novaPlaca)

            if opt3 == 2:
                print("Insira o novo valor: ")
                novoAnoFabricacao = int(input())
                automovel.AtualizarCarroAnoFabricacao(placa, novoAnoFabricacao)

print("\nQuitting...")
