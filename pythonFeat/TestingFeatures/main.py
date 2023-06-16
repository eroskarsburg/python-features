def InterfaceCalculoMedia():
  print("\n############ EXERCÍCIO 1 ############\n")
  print("Bem-vindo ao programa para calcular sua média!\n----------\n")
  x = int(input("Insira a quantidade de notas que deseja calcular: "))

  notas = LeNota(x)
  print(f'Lista das notas inseridas: {notas}')

  media = CalculaMediaLista(notas)
  print(f'Media: {media}')


def InterfaceInformaAprovacao():
  print("\n############ EXERCÍCIO 2 ############\n")
  print(
    "Bem-vindo! Este programa informará se está aprovado ou não, conforme suas notas."
  )
  sum = ReadGradesAndSum()
  half = CalculateHalfTwoGrades(sum)
  if half >= 7 and half < 10:
    print(f'Sua média foi {half}! Aprovado!')
  elif half < 7:
    print(f'Sua média foi {half}! Reprovado.')
  elif half == 10:
    print(f'Sua média foi {half}! Aprovado com Distinção!')


def InterfaceCalculoSalarioLiquido():
  print("\n############ EXERCÍCIO 3 ############\n")
  print(
    "Bem-vindo! Aqui calcularemos seu Salário Líquido!\nValor ganho por hora: R$5,00\n----------\n"
  )
  valorPorHora = 5
  horasTrabalhadas = int(input("Insira seu banco de horas: "))
  CalculaSalarioLiquido(valorPorHora, horasTrabalhadas)


def InterfaceMercadoTabajara():
  print("\n############ EXERCÍCIO 4 ############\n")
  precoFileAteCincoKG = 4.9
  precoAlcatraAteCincoKG = 5.9
  precoPicanhaAteCincoKG = 6.9
  ###
  precoFileAcimaCincoKG = 5.8
  precoAlcatraAcimaCincoKG = 6.8
  precoPicanhaAcimaCincoKG = 7.8
  print(
    "Bem-vindo ao mercado Tabajara!\nVerifique as carnes disponíveis e compre a sua!\n"
  )
  print(
    f'\n--------\nAté 5KG:\n--------\n1. Filé Duplo -> R${precoFileAteCincoKG}'
  )
  print(f'2. Alcatra -> R${precoAlcatraAteCincoKG}')
  print(f'3. Picanha -> R${precoPicanhaAteCincoKG}')
  print(
    f'\n-------------\nAcima de 5KG:\n-------------\n1. Filé Duplo -> R${precoFileAcimaCincoKG}'
  )
  print(f'2. Alcatra -> R${precoAlcatraAcimaCincoKG}')
  print(f'3. Picanha -> R${precoPicanhaAcimaCincoKG}')

  opcaoCarne = int(input("\nEscolha o tipo de carne que desejas: "))

  valorTotal = 0

  if opcaoCarne == 1:
    #File
    quantCarne = int(input("Insira a quantidade (KG): "))
    tipoCarne = "Filé Duplo"
    if quantCarne < 5:
      valorTotal = quantCarne * precoFileAteCincoKG
    else:
      valorTotal = quantCarne * precoFileAcimaCincoKG
  elif opcaoCarne == 2:
    #Alcatra
    quantCarne = int(input("Insira a quantidade (KG): "))
    tipoCarne = "Alcatra"
    if quantCarne > 5:
      valorTotal = quantCarne * precoAlcatraAteCincoKG
    else:
      valorTotal = quantCarne * precoAlcatraAcimaCincoKG
  elif opcaoCarne == 3:
    #Picanha
    quantCarne = int(input("Insira a quantidade (KG): "))
    tipoCarne = "Picanha"
    if quantCarne > 5:
      valorTotal = quantCarne * precoPicanhaAteCincoKG
    else:
      valorTotal = quantCarne * precoPicanhaAcimaCincoKG
  else:
    return print("Opção inválida.")

  print(f'Valor total a pagar: R${valorTotal}')

  print(
    "\n----------\n1. Dinheiro\n2. Crédito\n3. Cartão Tabajara (5% Desconto)\n----------\n"
  )

  opcaoPagamento = int(input("Escolha a forma de pagamento: "))

  if opcaoPagamento == 1:
    tipoPagamento = "Dinheiro"
    valorDesconto = "0"
  elif opcaoPagamento == 2:
    tipoPagamento = "Crédito"
    valorDesconto = "0"
  elif opcaoPagamento == 3:
    tipoPagamento = "Cartão Tabajara"
    valorDesconto = valorTotal * 0.05
    valorTotal = valorTotal - (valorTotal * 0.05)
  else:
    return print("Tipo de pagamento incorreto.")

  print("\n---------------\nInformações da Compra:\n---------------")
  print(f'Tipo de carne: {tipoCarne}')
  print(f'Quantidade: {quantCarne}KG')
  print(f'Preço total: R${valorTotal}')
  print(f'Tipo de pagamento: {tipoPagamento}')
  print(f'Valor do desconto: R${valorDesconto}')


def InterfaceCaixaTabajara():
  print("\n############ EXERCÍCIO 5 ############\n")
  x = 1
  while x == 1:
    InsereItens()
    print("\nDigite (1) para SIM\nDigite (0) para NÃO\n")
    x = int(input("Deseja registrar outro pagamento? "))
    if x == 0:
      return print("\nSaindo do programa...")
    elif x == 1:
      c = 0
    else:
      print("\nOpção inválida. Saindo do programa...")


def InterfaceDividaAndParcelas():
  print("\n############ EXERCÍCIO 6 ############\n")
  listValorDivida, listValorTotalParcela, listValorJuros, listQntParcelas = [], [], [], []
  valorJuros = 0
  valorTotalParcela = 0
  cc = 1
  while cc == 1:
    divida = float(input("Insira o valor da dívida: "))
    parcelas = int(
      input("Insira a quantidade de parcelas (1, 3, 6, 9 ou 12): "))
    if parcelas == 1:
      listValorDivida.append(divida)
      listQntParcelas.append(parcelas)
      listValorTotalParcela.append(divida)
      listValorJuros.append(valorJuros)
      cc = int(
        input(
          "\nDeseja inserir mais uma dívida?\nDigite (1) para SIM\nDigite (0) para NÃO\n"
        ))
    elif parcelas == 3:
      listValorDivida.append(divida)
      listQntParcelas.append(parcelas)
      valorTotalParcela = divida / parcelas
      listValorTotalParcela.append(valorTotalParcela)
      valorJuros = divida * 0.1
      listValorJuros.append(valorJuros)
      cc = int(
        input(
          "\nDeseja inserir mais uma dívida?\nDigite (1) para SIM\nDigite (0) para NÃO\n"
        ))
    elif parcelas == 6:
      listValorDivida.append(divida)
      listQntParcelas.append(parcelas)
      valorTotalParcela = divida / parcelas
      listValorTotalParcela.append(valorTotalParcela)
      valorJuros = divida * 0.15
      listValorJuros.append(valorJuros)
      cc = int(
        input(
          "\nDeseja inserir mais uma dívida?\nDigite (1) para SIM\nDigite (0) para NÃO\n"
        ))
    elif parcelas == 9:
      listValorDivida.append(divida)
      listQntParcelas.append(parcelas)
      valorTotalParcela = divida / parcelas
      listValorTotalParcela.append(valorTotalParcela)
      valorJuros = divida * 0.2
      listValorJuros.append(valorJuros)
      cc = int(
        input(
          "\nDeseja inserir mais uma dívida?\nDigite (1) para SIM\nDigite (0) para NÃO\n"
        ))
    elif parcelas == 12:
      listValorDivida.append(divida)
      listQntParcelas.append(parcelas)
      valorTotalParcela = divida / parcelas
      listValorTotalParcela.append(valorTotalParcela)
      valorJuros = divida * 0.25
      listValorJuros.append(valorJuros)
      cc = int(
        input(
          "\nDeseja inserir mais uma dívida?\nDigite (1) para SIM\nDigite (0) para NÃO\n"
        ))
    else:
      return print("\nValor incorreto de parcelas.\n")

  for i in range(len(listValorDivida)):
    print(f'Dívida: {listValorDivida[i]}')
    print(f'Valor juros: {listValorJuros[i]}')
    print(f'Quantidade Parcelas: {listQntParcelas[i]}')
    print(f'Valor da parcela: {listValorTotalParcela[i]}')
    print("\n------------------\n")


def InterfaceCardapioLanchonete():
  print("\n############ EXERCÍCIO 7 ############\n\n")
  print("######### Cardápio #########")
  print("Especificação    Código    Preço")
  print("----------------------------------")
  print("Cachorro Quente  100       R$1,20")
  print("Bauru simples    101       R$1,30")
  print("Bauru com ovo    102       R$1,50")
  print("Hamburguer       103       R$1,20")
  print("Cheeseburguer    104       R$1,30")
  print("Refrigerante     105       R$1,00")
  print("----------------------------------")

  listNomePedidos, listPrecoPedidos = [], []
  preco = 0
  vv = 1
  totalPedido = 0
  totalGeral = 0

  while vv == 1:
    codigo = int(input("Insira o código do produto escolhido: "))
    if codigo == 100:
      nomePedido = "Cachorro Quente"
      quantidadePedido = int(input("Insira a quantidade: "))
      preco = 1.2
      totalPedido = preco * quantidadePedido
      listPrecoPedidos.append(totalPedido)
      listNomePedidos.append(nomePedido)
    elif codigo == 101:
      nomePedido = "Bauru Simples"
      quantidadePedido = int(input("Insira a quantidade: "))
      preco = 1.3
      totalPedido = preco * quantidadePedido
      listPrecoPedidos.append(totalPedido)
      listNomePedidos.append(nomePedido)
    elif codigo == 102:
      nomePedido = "Bauru com ovo"
      quantidadePedido = int(input("Insira a quantidade: "))
      preco = 1.5
      totalPedido = preco * quantidadePedido
      listPrecoPedidos.append(totalPedido)
      listNomePedidos.append(nomePedido)
    elif codigo == 103:
      nomePedido = "Hamburguer"
      quantidadePedido = int(input("Insira a quantidade: "))
      preco = 1.2
      totalPedido = preco * quantidadePedido
      listPrecoPedidos.append(totalPedido)
      listNomePedidos.append(nomePedido)
    elif codigo == 104:
      nomePedido = "Cheeseburguer"
      quantidadePedido = int(input("Insira a quantidade: "))
      preco = 1.3
      totalPedido = preco * quantidadePedido
      listPrecoPedidos.append(totalPedido)
      listNomePedidos.append(nomePedido)
    elif codigo == 105:
      nomePedido = "Refrigerante"
      quantidadePedido = int(input("Insira a quantidade: "))
      preco = 1
      totalPedido = preco * quantidadePedido
      listPrecoPedidos.append(totalPedido)
      listNomePedidos.append(nomePedido)
    else:
      print("\nValor incorreto. Tente novamente.\n")
      vv = 1
    vv = int(
      input(
        "\nDeseja adicionar mais compras?\nDigite (1) para SIM\nDigite (0) para NÃO\n> "
      ))

  somaPedidos = 0
  for i in range(len(listNomePedidos)):
    somaPedidos += listPrecoPedidos[i]
    print("\n------------------")
    print(f'Nome do pedido: {listNomePedidos[i]}')
    print(f'Preço: R${listPrecoPedidos[i]}')
    print("------------------")
  print(f'\nValor total das compras: R${somaPedidos}')


#======#


def CalculaTroco(total):
  dinheiro = float(input("Dinheiro: "))
  while dinheiro < total:
    print("\nValor menor que o total. Digite novamente.\n")
    dinheiro = float(input("Dinheiro: "))
  troco = dinheiro - total
  return print(f'\n> Troco: {troco}')


def VerificaTotalItens(listTotal):
  if listTotal == 0:
    return print("\n* Valor total de itens inválido. *\n")


def CalculaTotalItens(listValorTotalItens, listQntItens):
  valorTotalItens = 0
  for i in range(len(listValorTotalItens)):
    valorTotalItens += listValorTotalItens[i]
    print(f'Produto {listQntItens[i]}: R${listValorTotalItens[i]}')

  if valorTotalItens == 0:
    return print("\n* Valor total de itens inválido. *\n")

  tot = round(valorTotalItens, 2)
  print(f'Total a pagar: R${tot}\n')
  z = CalculaTroco(valorTotalItens)
  return z


def InsereItens():
  print("\n#####CAIXA#####\n")
  print("* Insira os preços dos itens a calcular.\n")
  print("* Digite 0 (ZERO) caso deseje finalizar a conta.\n")
  listaContItens, listaValores = [], []
  valorItem = 1
  cont = 1
  try:
    while valorItem > 0:
      valorItem = float(input("> "))
      if valorItem == 0 or valorItem == '':
        x = CalculaTotalItens(listaValores, listaContItens)
        return x
      listaValores.append(valorItem)
      listaContItens.append(cont)
      cont += 1
  except ValueError:
    if valorItem == '':
      print("\nVocê digitou um valor incorreto. Fechando programa.\n")
    else:
      print(
        "\nIdentificamos um erro. Por segurança iremos reiniciar o pagamento.")


def ReadGradesAndSum():
  fstGrade = float(input("Digite a primeira nota: "))
  scndGrade = float(input("Digite a segunda nota: "))

  sum = fstGrade + scndGrade
  return sum


def CalculateHalfTwoGrades(sum):
  halfGrades = sum / 2
  return halfGrades


def LeNota(qtdNotas):
  notasTotais = []
  aux = 1
  for i in range(qtdNotas):
    nota = float(input(f'Insira a {aux}ª nota: '))
    notasTotais.append(nota)
    aux += 1
  return notasTotais


def CalculaMediaLista(listaNotas):
  soma = 0
  for i in range(len(listaNotas)):
    soma = soma + listaNotas[i]
  return (soma / len(listaNotas))


def CalculaSalarioLiquido(valorHora, horasTrabalhadas):
  salarioBruto = valorHora * horasTrabalhadas
  impostoRenda = 0
  descontos = 0

  if salarioBruto <= 900:
    impostoRenda = 0
    descontos += impostoRenda
  elif salarioBruto > 900 and salarioBruto <= 1500:
    impostoRenda = salarioBruto * 0.05
    descontos += impostoRenda
  elif salarioBruto > 1500 and salarioBruto <= 2500:
    impostoRenda = salarioBruto * 0.1
    descontos += impostoRenda
  else:
    impostoRenda = salarioBruto * 0.2
    descontos += impostoRenda

  inss = salarioBruto * 0.1
  fgts = salarioBruto * 0.11
  descontos += inss

  salarioLiquido = salarioBruto - descontos
  # Imprime na tela
  print(f'Salário bruto: R${salarioBruto}')
  print(f'(+) FGTS: R${fgts}')
  print(f'(-) INSS: R${inss}')
  print(f'(-) IR: R${impostoRenda}')
  print(f'Total de descontos: R${descontos}')
  print(f'Salário líquido: R${salarioLiquido}')


## Processamento Main >

#InterfaceCalculoMedia()
#InterfaceInformaAprovacao()
#InterfaceCalculoSalarioLiquido()
#InterfaceMercadoTabajara()
#InterfaceCaixaTabajara()
InterfaceDividaAndParcelas()
#InterfaceCardapioLanchonete()