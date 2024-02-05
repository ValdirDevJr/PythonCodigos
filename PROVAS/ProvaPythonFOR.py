# Desenvolva um programa que leia o nome, idade e sexo de 5 pessoas. No final do programa, exiba:

#- A média de idade de todo o grupo.

#- Qual o nome da pessoa mais velha.

#- Quantas pessoas têm menos de 20 anos.

#- Quantas pessoas têm mais de 40 anos.

#- Qual o sexo da pessoa mais nova.

# Inicializa as variáveis para cálculos
soma_idades = 0
idade_mais_velha = 0
nome_mais_velha = ""
pessoas_menos_de_20 = 0
pessoas_mais_de_40 = 0
idade_mais_nova = float('inf')
sexo_mais_nova = ""
sexo_mais_velha = ""

# Usa um loop para ler informações de 5 pessoas
for i in range(1, 6):
    print(f"Digite as informações da {i}º pessoa:")
    
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ")
    
    # Calcula a média das idades
    soma_idades += idade
    
    # Verifica se é a pessoa mais velha
    if idade > idade_mais_velha:
        idade_mais_velha = idade
        nome_mais_velha = nome
        sexo_mais_velha = sexo
    
    # Verifica a idade e o sexo da pessoa mais nova
    if idade < idade_mais_nova:
        idade_mais_nova = idade
        sexo_mais_nova = sexo
    
    # Verifica se a pessoa tem menos de 20 anos
    if idade < 20:
        pessoas_menos_de_20 += 1
    
    # Verifica se a pessoa tem mais de 40 anos
    if idade > 40:
        pessoas_mais_de_40 += 1

# Calcula a média de idade
media_idades = soma_idades / 5

# Exibe os resultados
print(f"Média de idade do grupo: {media_idades:.2f} anos")
print(f"Pessoa mais velha: {nome_mais_velha} com {idade_mais_velha} anos (sexo: {sexo_mais_velha})")
print(f"Pessoas com menos de 20 anos: {pessoas_menos_de_20}")
print(f"Pessoas com mais de 40 anos: {pessoas_mais_de_40}")
print(f"Pessoa mais nova: Sexo {sexo_mais_nova}")