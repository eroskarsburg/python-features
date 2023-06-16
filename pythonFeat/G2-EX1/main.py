#EROS KARSBURG DIAS DA ROSA
#EXERCÍCIO STRING

str = 'X-DSPAM-Confidence: 0.8475'
# Encontra a posição dos dois pontos e adiciona 2 para obter o início do número e retirar o espaço entre : e 0.8475
stringEncontrada = str.find(':') + 2
# Extrai a parte da string selecionada e converte para float ('0.8475')
stringConvertidaFloat = float(str[stringEncontrada:])

print(f'===========\nString = {str}\n===========')
print(f'String encontrada: "{str[stringEncontrada:]}"')
print(f'Tipo da variável: {type(str[stringEncontrada:])}')
print(f'===========\nString convertida para Float: {stringConvertidaFloat}')
print(f'Tipo da variável: {type(stringConvertidaFloat)}')
