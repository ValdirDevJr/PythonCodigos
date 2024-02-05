# Faça um programa que solicite ao usuário que digite 10 valores para
# preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.
# reponda para mim

# Cria uma lista vazia
numeros = []

# Solicita ao usuário que insira 10 valores
for i in range(10):
    valor = int(input(f'Digite o {i+1}º valor: '))
    numeros.append(valor)

# Separa os números pares e ímpares
numeros_pares = [num for num in numeros if num % 2 == 0]
numeros_impares = [num for num in numeros if num % 2 != 0]

# Exibe os números pares
print('Números pares:', numeros_pares)

# Exibe os números ímpares como uma tupla
print('Números ímpares:', tuple(numeros_impares))

# Exibe a quantidade de números pares e ímpares
print('Quantidade de números pares:', len(numeros_pares))
print('Quantidade de números ímpares:', len(numeros_impares))

# Calcula e exibe a soma dos números pares e ímpares
soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impares)
print('Soma dos números pares:', soma_pares)
print('Soma dos números ímpares:', soma_impares)