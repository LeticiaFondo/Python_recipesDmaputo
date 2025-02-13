#Criacao de Classes
class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo #atributo
        self.cor = cor  #atributo

    def ligar(self): #metodo
        print(f'O carro {self.modelo} {self.cor} esta ligado')

    