import random


def nested_sum(ftList):
  x, z = 0, 0
  for x in range(len(ftList)):
    y = sum(ftList[x])
    z += y
  return z


def cumSum(list):
  x = 0
  for x in range(len(list)):
    if (x + 1) == len(list):
      return list
    soma = list[x] + list[x + 1]
    list[x + 1] = soma
    soma = 0
  return list


def middle(list):
  list.remove(max(list))
  list.remove(min(list))
  return list


def chop(list):
  for x in range(len(list)):
    if len(list) == 0:
      return list
  list.remove(max(list))
  list.remove(min(list))


def is_sorted(list):
  return list == sorted(list)


def is_anagram(string, string2):
  return sorted(string) == sorted(string2)


def has_duplicated(list):
  return len(list) != len(set(list))


def has_duplicate_birthdays(num_students):
  birthdays = []
  for _ in range(num_students):
    birthday = random.randint(1, 365)
    if birthday in birthdays:
      return True
    birthdays.append(birthday)
  return False


def estimate_probability(num_simulations, num_students):
  count_duplicates = 0
  for _ in range(num_simulations):
    if has_duplicate_birthdays(num_students):
      count_duplicates += 1
  probability = count_duplicates / num_simulations
  return probability


def read_words_append():
  words_list = []
  with open("words.txt", "r") as file:
    for line in file:
      word = line.strip()
      words_list.append(word)
  return words_list


def read_words_concatenate():
  words_list = []
  with open("words.txt", "r") as file:
    for line in file:
      word = line.strip()
      words_list = words_list + [word]
  return words_list


def in_bisect(sorted_list, target):
  low = 0
  high = len(sorted_list) - 1

  while low <= high:
    mid = (low + high) // 2
    mid_value = sorted_list[mid]

    if mid_value == target:
      return mid
    elif mid_value < target:
      low = mid + 1
    else:
      high = mid - 1

  return None


def find_reverse_pairs(word_list):
  reverse_pairs = []
  for word in word_list:
    reverse_word = word[::-1]
    if reverse_word in word_list:
      reverse_pairs.append((word, reverse_word))
  return reverse_pairs


#----------------------------


def exercicio1():
  print("\nEXERCÍCIO 1\n")
  fstList, scndList, thrdList = [2, 6, 8], [1, 2, 3], [8, 5, 3]
  fatherList = [fstList, scndList, thrdList]
  print(f'1°: {fstList}\n2°: {scndList}\n3°: {thrdList}')
  print(f'A soma é: {nested_sum(fatherList)}.')


def exercicio2():
  print("\nEXERCÍCIO 2\n")
  list = [2, 5, 6, 7, 8]
  print(f'Lista: {list}')
  print(f'Lista modificada: {cumSum(list)}')


def exercicio3():
  print("\nEXERCÍCIO 3\n")
  list = [1, 3, 4, 6, 7, 9]
  print(f'Lista: {list}')
  print(f'Lista modificada: {middle(list)}')


def exercicio4():
  print("\nEXERCÍCIO 4\n")
  list = [2, 7, 8, 12, 13, 13]
  print(f'Lista: {list}')
  print(f'Lista modificada: {chop(list)}')


def exercicio5():
  print("\nEXERCÍCIO 5\n")
  list = [2, 7, 8, 12]
  print(f'Lista: {list}')
  print(f'Ordenada: {is_sorted(list)}')
  listLetters = ['a', 'b', 'c', 'a']
  print(f'Lista: {listLetters}')
  print(f'Ordenada: {is_sorted(listLetters)}')


def exercicio6():
  print("\nEXERCÍCIO 6\n")
  fstString = "abcde"
  scndString = "cdabe"
  print(f'Strings: {fstString}, {scndString}')
  print(f'São Anagramas: {is_anagram(fstString, scndString)}')


def exercicio7():
  print("\nEXERCÍCIO 7\n")
  list = [2, 7, 8, 12]
  print(f'Lista: {list}')
  print(f'Caracteres duplicados? {has_duplicated(list)}')


def exercicio8():
  print("\nEXERCÍCIO 8\n")
  num_simulations = 10000
  num_students = 23
  print(f'Estudantes: {num_students}')
  probability = estimate_probability(num_simulations, num_students)
  print(f"A probabilidade estimada é de {probability:.4f}")


def exercicio9():
  print("\nEXERCÍCIO 9\n")
  #read_words_append()
  #read_words_concatenate()
  print(
    "- A primeira versão que utiliza o método 'append()' é mais eficiente. Isso ocorre porque o método append() adiciona elementos à lista existente, modificando-a in-place. Por outro lado, a expressão t = t + [x] cria uma nova lista a cada iteração e atribui-a novamente à variável t, o que gera uma cópia desnecessária da lista."
  )


def exercicio10():
  print("\nEXERCÍCIO 10\n")
  list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
  ]
  target = 13
  print(f'Lista: {list}')
  print(f'Valor alvo: {target}')
  print(f'Índice do valor alvo: {in_bisect(list, target)}')


def exercicio11():
  print("\nEXERCÍCIO 11\n")
  wordsList = [
    "eros", "maria", "escola", "lasalle", "ellasal", "sore", "aleatorio",
    "airam"
  ]
  print(f'Lista de palavras: {wordsList}')
  print("\nPares inversos:")
  pairs = find_reverse_pairs(wordsList)
  for pair in pairs:
    print(pair)


#MAIN

exercicio1()
exercicio2()
exercicio3()
exercicio4()
exercicio5()
exercicio6()
exercicio7()
exercicio8()
exercicio9()
exercicio10()
exercicio11()
