num = int(input("Enter a number: "))

x, y, aux = num, num, num

for aux in range(num, 0, -1):
  for x in range(num, 0, -1):
    for y in range(num, 0, -1):
      if aux**2 == x**2 + y**2:
        print(f'{aux} is hypotenuse ans sides are {x} and {y}')

print('Código do cacete...')