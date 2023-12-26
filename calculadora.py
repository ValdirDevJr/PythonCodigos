#                      Calculadora


def somar(a, b):
    return a + b


def multiplicação(a, b):
    return a * b


def subtração(a, b):
    return a - b


def divisão(a, b):
    if b != 0:
        return a / b
    else:
        print('Erro: Divisão por zero')
        return None


while True:
    print(
        '''Escolha uma operação
          
[1] - Soma
[2] - Subtração
[3] - Multiplicação
[4] - Divisão
[5] - Sair

'''
    )

    escolha = input('Escolha a operação desejada: ')

    if escolha == '5':
        print('Calculadora encerrada')
        break

    if escolha not in ['1', '2', '3', '4']:
        print('Opção inválida. Tente novamente.')
        continue  # Volta ao início do loop sem solicitar num1 e num2

    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    match escolha:
        case '1':
            resultado = somar(num1, num2)
            print(f'{num1} + {num2} = {resultado}')

        case '2':
            resultado = subtração(num1, num2)
            print(f'{num1} - {num2} = {resultado}')

        case '3':
            resultado = somar(num1, num2)
            print(f'{num1} * {num2} = {resultado}')

        case '4':
            resultado = subtração(num1, num2)
            if resultado is not None:
                print(f'{num1} / {num2} = {resultado}')

        case _:
            ('Comando inválido. Tente novamente')
