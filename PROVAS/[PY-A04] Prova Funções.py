# [PY-A04] Desenvolva um programa em Python que permita ao usuário digitar várias notas. Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.


def calcular_media(a, b, c, d):
    return (a + b + c + d) / 4


def verificar_situacao():
    if resultado_média < 7:
        print("Reprovado")
    elif resultado_média >= 7:
        print("Aprovado")
    elif resultado_média == 10:
        print("Parabéns, sua média é 10!")


nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

resultado_média = calcular_media(nota1, nota2, nota3, nota4)
print(f"Média: {resultado_média}")
