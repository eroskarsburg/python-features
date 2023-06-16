import math

print("\nEX1:\n")
y = float(input("Digite um número: "))
x = 1
while y > 1:
  x *= y
  y -= 1
print("Fatorial:", x)


print("\n=============\n\nEX2:\n")
erro = int(input("Digite um número real: "))
cont = 0;
x = 1
somaFatorial = 0
while erro > cont:
  x *= y
  cont -= 1
print("Fatorial:", x)

#print(math.factorial(0))

#print("\n=============\n\nEX2:\n")

#erro = float(input("Insira um número real: "))
#x = 1
#y = 0
#z=0
#while erro != -1:
#  z = erro
#  x += (1/z)
#  erro -= 1
#print("Fatorial:", z)
#print("Fatorial Real:", x)