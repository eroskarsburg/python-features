class Montadora:
    def __init__(self, codigoMontadora=0, estado=None, razaoSocial=None):
        self.CodigoMontadora = codigoMontadora
        self.Estado = estado
        self.RazaoSocial = razaoSocial

    def __str__(self):
        return f"-> Montadora:\nCódigo: {self.CodigoMontadora},\nEstado: {self.Estado},\nRazão Social: {self.RazaoSocial}"


class Modelo:
    def __init__(self, codigoModelo=0, nomeModelo=None, montadora=None):
        self.CodigoModelo = codigoModelo
        self.NomeModelo = nomeModelo
        self.Montadora = montadora

    def __str__(self):
        if self.Montadora is not None:
            return f"-> Modelo:\nCódigo: {self.CodigoModelo},\nNome: {self.NomeModelo},\nCódigo Montadora: {self.Montadora.CodigoMontadora},\nRazão Social Montadora: {self.Montadora.RazaoSocial},\nEstado Montadora: {self.Montadora.Estado}"
        else:
            return f"-> Modelo:\nCódigo: {self.CodigoModelo},\nNome: {self.NomeModelo},\nMontadora: None"


class Carro:
    def __init__(self, placa=None, modelo=None, anoFabricacao=0):
        self.Placa = placa
        self.Modelo = modelo
        self.AnoFabricacao = anoFabricacao

    def __str__(self):
        if self.Modelo is not None and self.Modelo.Montadora is not None:
            return f"-> Carro:\nPlaca: {self.Placa},\nCódigo Modelo: {self.Modelo.CodigoModelo},\nNome Modelo: {self.Modelo.NomeModelo},\nCódigo Montadora: {self.Modelo.Montadora.CodigoMontadora},\nRazão Social Montadora: {self.Modelo.Montadora.RazaoSocial},\nEstado Montadora: {self.Modelo.Montadora.Estado},\nAno fabricação: {self.AnoFabricacao}"
        else:
            return f"-> Carro:\nPlaca: {self.Placa},\nModelo: None,\nAno fabricação: {self.AnoFabricacao}"


class Menus:
    def MenuBooksAndEditor(self):
        print("#### Menu ####")
        print("1. Cadastrar Editora: ")
        print("2. Cadastrar Livro: ")
        print("3. Pesquisar Editora: ")
        print("4. Pesquisar Livro: ")
        print("5. Sair: ")

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


class Automovel:
    def __init__(self):
        self.listaMontadora = []
        self.listaModelo = []
        self.listaCarro = []

    def MostrarAtributosAutomovel(self):
        for montadora in self.listaMontadora:
            print("\n", montadora)

        for modelo in self.listaModelo:
            print("\n", modelo)

        for carro in self.listaCarro:
            print("\n", carro, "\n")

    def CadastrarMontadora(self):
        try:
            print("### Montadora ###")
            print("-> Codigo:")
            montadora = Montadora()
            montadora.CodigoMontadora = int(input())  # Use input() in Python
            print("-> Razão Social:")
            montadora.RazaoSocial = input()  # Use input() in Python
            print("-> Estado:")
            montadora.Estado = input()  # Use input() in Python
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
            print("-> Codigo:")
            modelo = Modelo()
            modelo.CodigoModelo = int(input())  # Use input() in Python
            print("-> Nome do Modelo:")
            modelo.NomeModelo = input()  # Use input() in Python
            print("-> Código da Montadora:")
            codigoMontadora = int(input())  # Use input() in Python

            if not self.VerificarMontadoraExistente(codigoMontadora):
                print("Não há Montadora cadastrada com esse código.")
                return

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
            print("-> Placa:")
            carro = Carro()
            carro.Placa = input()  # Use input() in Python
            print("-> Ano de fabricação:")
            carro.AnoFabricacao = int(input())  # Use input() in Python
            print("-> Código do Modelo:")
            codigoModelo = int(input())  # Use input() in Python

            if not self.VerificarModeloExistente(codigoModelo):
                print("Não há Modelo cadastrado com esse código.")
                return

            self.listaCarro.append(carro)
            print("\nCadastro finalizado!\n")
        except Exception as ex:
            print(f"Ocorreu um erro.\nErro: {ex}")

    def VerificarMontadoraExistente(self, codigoMontadora):
        for montadora in self.listaMontadora:
            if montadora.CodigoMontadora == codigoMontadora:
                modelo = Modelo()
                modelo.Montadora = montadora
                self.listaModelo.append(modelo)
                return True
        return False

    def VerificarModeloExistente(self, codigoModelo):
        for modelo in self.listaModelo:
            if modelo.CodigoModelo == codigoModelo:
                carro = Carro()
                carro.Modelo = modelo
                self.listaCarro.append(carro)
                return True
        return False

    def BuscarMontadora(self, codigoMont):
        for montadora in self.listaMontadora:
            if montadora.CodigoMontadora == codigoMont:
                print("\nMontadora a ser atualizada: ")
                print(montadora)
                return True
        return False

    def BuscarModelo(self, codigoModelo):
        for modelo in self.listaModelo:
            if modelo.CodigoModelo == codigoModelo:
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

    def AtualizarMontadoraCodigo(self, codigo, novoCodigo):
        for montadora in self.listaMontadora:
            if montadora.CodigoMontadora == codigo:
                montadora.CodigoMontadora = novoCodigo
                print("\nMontadora Atualizada!\n")
                return

    def AtualizarMontadoraEstado(self, codigo, novoEstado):
        for montadora in self.listaMontadora:
            if montadora.CodigoMontadora == codigo:
                montadora.Estado = novoEstado
                print("\nMontadora Atualizada!\n")
                return

    def AtualizarMontadoraRazaoSocial(self, codigo, novaRazaoSocial):
        for montadora in self.listaMontadora:
            if montadora.CodigoMontadora == codigo:
                montadora.RazaoSocial = novaRazaoSocial
                print("\nMontadora Atualizada!\n")
                return

    def AtualizarModeloCodigo(self, codigo, novoCodigo):
        for modelo in self.listaModelo:
            if modelo.CodigoModelo == codigo:
                modelo.CodigoModelo = novoCodigo
                print("\nModelo Atualizado!\n")
                return

    def AtualizarModeloNome(self, codigo, novoNome):
        for modelo in self.listaModelo:
            if modelo.CodigoModelo == codigo:
                modelo.NomeModelo = novoNome
                print("\nModelo Atualizado!\n")
                return

    def AtualizarCarroPlaca(self, placa, novaPlaca):
        for carro in self.listaCarro:
            if carro.Placa == placa:
                carro.Placa = novaPlaca
                print("\nCarro Atualizado!\n")
                return

    def AtualizarCarroAnoFabricacao(self, placa, novoAnoFabricacao):
        for carro in self.listaCarro:
            if carro.Placa == placa:
                carro.AnoFabricacao = novoAnoFabricacao
                print("\nCarro Atualizado!\n")
                return


# Create an instance of Automovel class
automovel = Automovel()
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
