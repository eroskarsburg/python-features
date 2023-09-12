from product import Produto

def Menu():
    prod = Produto
    print("\n### MENU CADASTRO DE PRODUTOS ###\n")
    print("> O usuário deve informar os dados para instanciação dos produtos\n")
    codigoProduto = int(input("> Código do produto: "))
    descricaoProduto = input("> Descrição do produto: ")
    precoProduto = float(input("> Preço do produto: "))
    custoProduto = float(input("> Custo do produto: "))
    prod.produtoToString(codigoProduto, descricaoProduto, precoProduto, custoProduto)
    print(f"\n> Valor da margem de lucro: {prod.calculaMargem(precoProduto, custoProduto)}%")

    input("\n> Precione qualquer tecla para sair.")
