print("############## PROVA PRATICA ##############")


def PrimeiroExercicio():
  c = 1
  while c == 1:
    try:
      x = float(input("\nInsira o primeiro valor entre 0 e 10: "))
      if x >= 0 and x <= 10:
        print(f'O valor escolhido foi {x}!')
        c = 0
      else:
        print("\nValor incorreto. Digite novamente.")
    
    except ValueError:
      print(f'Valor incorreto: {ValueError}. Tente novamente!')
        



def SegundoExercicio():
  q = 1
  while q == 1:
    try:
      a = int(input("Insira o primeiro valor (positivo):"))
      b = int(input("Insira o segundo valor (positivo):"))
      c = int(input("Insira o terceiro valor (positivo):"))
      
      m1, m2, m3, m4 = 0, 0, 0, 0
      
      #verifica se é triangulo
      if a<b+c and b<a+c and c<b+a:
        m1 = 1
      #verifica equilatero
      if a==b and a==c and c==b:
        m2 = 1
      #verifica isosceles
      if (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
        m3 = 1
      #verifica escaleno
      if a!=b and a!=c and b!=c:
        m4 = 1
    
      if m1 == 1 and m2 == 1 and m3 != 1 and m4 != 1:
        print("Triângulo Equilátero")
        q=0
      if m1 == 1 and m2 != 1 and m3 == 1:
        print("Triângulo Isósceles")
        q=0
      if m1 == 1 and m2 != 1 and m3 != 1 and m4 == 1:
        print("Triângulo Escaleno")
        q=0
      if m1 != 1:
        print("Não é Triângulo")
        q=0
    except ValueError:
      print(f'Valor incorreto: {ValueError}. Tente novamente!')


def TerceiroExercicio():
  cont = 0
  maior = 0
  menor = 2293817
  c = 0
  soma = 0
  media = 0
  while cont != -1:
    x = int(input("Insira um valor inteiro positivo ou -1 para encerrar: "))
    if x == -1:
      cont = -1
    else:
      c += 1
      soma += x
      media = soma/c
      if x > maior:
        maior = x
      if x < menor:
        menor = x
      
  print(f'Foram digitados {c} números inteiros positivos')
  print(f'A soma dos números é {soma}')
  print(f'A média dos números é {media}')
  print(f'O menor número é {menor}')
  print(f'O maior número é {maior}')


def RetornaPouN(valor):
  if valor > 0:
    print("P")
  elif valor <= 0:
    print("N")


def QuartoExercicio():
  valor = int(input("Insira um valor negativo ou positivo: "))
  RetornaPouN(valor)



PrimeiroExercicio()
SegundoExercicio()
TerceiroExercicio()
QuartoExercicio()