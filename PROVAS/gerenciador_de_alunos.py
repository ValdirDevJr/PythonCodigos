# [PY-A07] Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. O programa deve permitir adicionar, remover, atualizar e listar os alunos.


# Para isso, você deve implementar um módulo que contém as seguintes funções:


# AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.


# RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.


# AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário .


# VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.


# Adiciionar Aluno
def AdicionarAluno(dicionario_alunos):

    matricula = input('Digite o número de matrícula do aluno: ')
    nome = input('Digite o nome do aluno: ')

    if matricula in dicionario_alunos:
        print(f'Aluno com matrícula {matricula} já cadastrado.')
    else:
        dicionario_alunos[matricula] = nome
    print(f'Aluno {nome} adicionado com sucesso.')


# Remover Aluno
def RemoverAluno(dicionario_alunos):

    matricula = input('Digite o número de matrícula do aluno a ser removido: ')

    if matricula not in dicionario_alunos:
        print(f'Aluno com matrícula {matricula} não encontrado.')
    else:
        del dicionario_alunos[matricula]
    print(f'Aluno com matrícula {matricula} removido com sucesso.')


# Atualizar Aluno
def AtualizarAluno(dicionario_alunos):

    matricula = input('Digite o número de matrícula do aluno a ser atualizado: ')

    if matricula not in dicionario_alunos:
        print(f'Aluno com matrícula {matricula} não encontrado.')
    else:
        novo_nome = input('Digite o novo nome do aluno: ')
        dicionario_alunos[matricula] = novo_nome
        print(f'Nome do aluno com matrícula {matricula} atualizado com sucesso.')


# Ver Alunos
def VerAlunos(dicionario_alunos):

    if not dicionario_alunos:
        print('Nenhum aluno cadastrado.')
    else:
        print('~~~^[Lista de Alunos]^~~~')
    for matricula, nome in dicionario_alunos.items():
        print(f'Matrícula: {matricula} - Nome: {nome}')


# Dicionário para armazenar os alunos
dicionario_alunos = {}

while True:
    print(
        '''
~~~^[Menu de opções]^~~~
[1] - Adicionar aluno
[2] - Remover aluno
[3] - Atualizar aluno
[4] - Ver alunos
[5] - Sair
'''
    )

    opcao = input('Digite a opção desejada: ')

    match opcao:
        case '1':
            AdicionarAluno(dicionario_alunos)
        case '2':
            RemoverAluno(dicionario_alunos)
        case '3':
            AtualizarAluno(dicionario_alunos)
        case '4':
            VerAlunos(dicionario_alunos)
        case '5':
            print('Obrigado por usar o gerenciador de dicionário de alunos!')
            break
        case _:
            print('Opção inválida.')
