class Produto:
    def __init__(self, codigo_produto: int, descricao, preco: float, custo: float):
        self.codigo_produto = codigo_produto
        self.descricao = descricao
        self.preco = preco
        self.custo = custo
# SETTERS
    def setCodigoProduto(self, codigo_produto: int):
        self.codigo_produto = codigo_produto
    def setDescricao(self, descricao):
        self.descricao = descricao
    def setPreco(self, preco: float):
        self.preco = preco
    def setCusto(self, custo: float):
        self.custo = custo
# GETTERS
    def getCodigoProduto(self):
        self.codigo_produto
    def getDescricao(self):
        self.descricao
    def getPreco(self):
        self.preco
    def getCusto(self):
        self.custo
# METHODS
    def calculaMargem(preco: float, custo: float):
        return "{:.2f}".format((custo/preco)*100)
    def produtoToString(codigo_produto: int, descricao, preco: float, custo: float):
        return print(f"\n### Item(s): ###\nCódigo do produto: {codigo_produto},\nDescrição do produto: {descricao},\nPreço do produto: {preco},\nCusto do produto: {custo}.")
