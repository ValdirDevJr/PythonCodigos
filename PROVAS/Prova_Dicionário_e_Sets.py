alunos = {}

def adicionar_aluno():
    nome = input('Digite o nome do aluno: ')
    matricula = input('Digite o número de matrícula do aluno: ')
    alunos[matricula] = nome
    print(f'Aluno {nome} adicionado com sucesso!\n')

def remover_aluno():
    matricula = input('Digite o número de matrícula do aluno a ser removido: ')
    if matricula in alunos:
        nome_aluno = alunos.pop(matricula)
        print(f'Aluno {nome_aluno} removido com sucesso!\n')
    else:
        print('Aluno não encontrado.\n')

def visualizar_alunos():
    print('\nLista de Alunos:')
    for matricula, nome in alunos.items():
        print(f'Matrícula: {matricula}, Nome: {nome}')
    print()

def main():
    while True:
        print('1. Adicionar Aluno')
        print('2. Remover Aluno')
        print('3. Visualizar Alunos')
        print('4. Sair')
        
        opcao = input('\nEscolha uma opção: ')

        if opcao == '1':
            adicionar_aluno()
        elif opcao == '2':
            remover_aluno()
        elif opcao == '3':
            visualizar_alunos()
        elif opcao == '4':
            print('Programa encerrado.')
            break
        else:
            print('Opção inválida. Tente novamente.\n')
