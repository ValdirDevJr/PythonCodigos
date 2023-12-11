# ~~~~~~~~~~~~~~~~~~ DESAFIO PRÁTICO ~~~~~~~~~~~~~~~~~~
#                      Calculadora

# Crie uma calculadora com opções de soma, multiplicação, subtração, divisão e sair.

# (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.)

# Utilize funções de rotina para cada operação e funções de unidade lógica para realizar os cálculos.

# Dica:
# Utilize de condicionais e Laços de Repetição para realizar esse exercício.


def somar(a, b):
    return a + b


def multiplicação(a, b):
    return a * b


def subtração(a, b):
    return a - b


def divisão(a, b):
    return a / b


while True:
    print("Escolha uma operação:")
    print("[1] - Soma")
    print("[2] - Subtração")
    print("[3] - Multiplicação")
    print("[4] - Divisão")
    print("[5] - Sair")

    escolha = input("Escolha a operação desejada: ")

    if escolha == "5":
        print("Calculadora encerrada")
        break

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if escolha == "1":
        resultado = somar(num1, num2)
        print(f"{num1} + {num2} = {resultado}")

    if escolha == "2":
        resultado = subtração(num1, num2)
        print(f"{num1} - {num2} = {resultado}")

    if escolha == "3":
        resultado = somar(num1, num2)
        print(f"{num1} * {num2} = {resultado}")

    if escolha == "4":
        resultado = subtração(num1, num2)
        print(f"{num1} / {num2} = {resultado}")

    else:
        ("Comando inválido. Tente novamente")
