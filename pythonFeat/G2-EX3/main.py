#EROS KARSBURG DIAS DA ROSA

def ler_palavras():
  dicionario = {}
  try:
    with open("words.txt", "r") as arquivo:
      for palavra in arquivo:
        palavra = palavra.strip()
        dicionario[palavra] = None
    return dicionario
  except FileNotFoundError:
    print("O arquivo words.txt não foi encontrado.")
    return None


def rotacionar_palavra(palavra, deslocamento):
  nova_palavra = ""
  for letra in palavra:
    if letra.isalpha():
      codigo = ord(letra) + deslocamento
      if letra.islower():
        if codigo > ord('z'):
          codigo -= 26
        elif codigo < ord('a'):
          codigo += 26
      else:
        if codigo > ord('Z'):
          codigo -= 26
        elif codigo < ord('A'):
          codigo += 26
      nova_palavra += chr(codigo)
    else:
      nova_palavra += letra
  return nova_palavra


def encontrar_pares_rotacionados(lista_palavras):
  pares_rotacionados = []
  for palavra in lista_palavras:
    for deslocamento in range(1, 26):  # Testa deslocamentos de -25 a 25
      palavra_rotacionada = rotacionar_palavra(palavra, deslocamento)
      if palavra_rotacionada in lista_palavras:
        pares_rotacionados.append((palavra, palavra_rotacionada))
  return pares_rotacionados


def invert_dict(dicionario):
  inverted_dict = {}
  for chave, valor in dicionario.items():
    inverted_dict.setdefault(valor, []).append(chave)
  return inverted_dict


def has_duplicates(lst):
  seen = {}
  for item in lst:
    if item in seen:
      return True
    seen[item] = True
  return False


def readAndWriteFile(archieve):
  writeFile = open(f'{archieve}', 'w')
  writeFile.write(
    '\nfrom stephen.marquard@uct.ac.za sat jan 5 09:14:16 2008\n')
  writeFile.write('return path: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>\n')
  writeFile.write('received: from murder (main.umich.edu [141.211.14.90])\n')
  writeFile.write('by FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA\n')
  writeFile.write('sat, 05 jan 2008 09:14:16 -0500')
  writeFile.close()
  with open(f'{archieve}', 'r', encoding="utf-8") as file:
    content = file.read()
    print(content.upper())


def aula29_05():
  print("\n======= Aula dia 29/05 =======\n")


def aula05_06():
  print("\n======= Aula dia 05/06 =======\n")


def ex1():
  print("\nEX: 1 ===========\n")
  dicionario_palavras = ler_palavras()
  if dicionario_palavras is not None:
    palavra = input(
      "Digite uma palavra para verificar se está no dicionário: ")
    if palavra in dicionario_palavras:
      print("A palavra está no dicionário!")
    else:
      print("A palavra não está no dicionário.")


def ex2():
  print("\nEX: 2 ===========\n")
  dictionary = {"chave1", "olá mundo"}
  invert_dict(dictionary)


def ex3():
  print("\nEX: 3 ===========\n")
  list = ["eros", "escola", "lasalle", "escola", "jogos", "lasalle"]
  print(f'Possui duplicado: {has_duplicates(list)}')


def ex4():
  print("\nEX: 4 ===========\n")
  lista_palavras = ["cheer", "melon", "jolly", "cubed", "HAL", "IBM"]
  pares_rotacionados = encontrar_pares_rotacionados(lista_palavras)
  for par in pares_rotacionados:
    print(f"Pares rotacionados: {par[0]}, {par[1]}")


def ex1_2():
  print("\nEX: 1 ===========\n")
  option = input("Digite o arquivo que deseja abrir: ")
  if ".txt" in option:
    print(f'option: {option}')
    readAndWriteFile(option)
  else:
    option = option + ".txt"
    print(f'option: {option}')
    readAndWriteFile(option)


# MAIN
aula29_05()
ex1()
ex2()
ex3()
ex4()

#+++++

aula05_06()
ex1_2()
