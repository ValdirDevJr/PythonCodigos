class Elevador():
    def __init__(self, totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = 0
        self.totalAndar = totalAndar
        self.atualAndar = 0
        
        
    def subir(self):
        if self.atualAndar < self.totalAndar:
            self.atualAndar += 1
            print('Subindo')
        else:
            print('VOCÊ ESTÁ NO ANDAR MAIS ALTO!')
            
            
    def descer(self):
        if self.atualAndar > 0:
            self.atualAndar -= 1
            print('Descendo')
        else:
            print('VOCÊ JÁ ESTÁ NO TÉRREO')
            
            
    def entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
        else:
            print('O ELEVADOR ESTÁ CHEIO')
            
            
    def sair(self):
        if self.atualCapacidade > self.totalCapacidade:
            self.atualCapacidade -= 1
        else:
            print('NÃO TEM NINGUÉM')

elevador = Elevador(10, 5)

elevador.subir()
elevador.descer()
elevador.entrar()
elevador.subir()
elevador.sair()

