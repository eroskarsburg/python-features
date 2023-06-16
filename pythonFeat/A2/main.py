print("EX. 2\n")
x = int(input("Definindo se o número é primo ou não.\nDigite um número: "))
z = x
contPrimo = 0

while x > 0:
  if z % x == 0:
    print("Divisível: ", x)
    x -= 1
    contPrimo += 1
  else:
    x -= 1

if contPrimo == 2:
  print(f"\nO número {z} é primo.")
else:
  print(f"\nO número {z} NÃO é primo.")
