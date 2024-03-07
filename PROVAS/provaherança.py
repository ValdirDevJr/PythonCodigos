class Material:
    def __init__(self, titulo, autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora
        
    def exibirInformacoes(self):
        print(f'Título: {self.titulo}')
        print(f'Autor/Editora: {self.autor_ou_editora}')
        
        
class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero
        
    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f'Gênero: {self.genero}')
        
        
class Revista(Material):
    def __init__(self, titulo, autor_ou_editora, edicao):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao
        
    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f'Edição: {self.edicao}')
        
        
livro = Livro('O Senhor dos Anéis', 'J.R.R Tolkien', 'Fantasia')
revista = Revista('Veja', 'Editora Abril', 'Edição 3000')

print('Detalhes do Livro:')
livro.exibirInformacoes()
print('\nDetalhes da Revista:')
revista.exibirInformacoes()