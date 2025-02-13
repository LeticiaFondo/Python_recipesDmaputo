#criacao da class
#o SELF
class Pessoa:
    #passando os parametros tudo o que esta dentro de parenteses
    # o init sao os paramentros que estao dentro do p1 = pessoa()
    def __init__(self, nome, idade, comendo = False, falar = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falar = falar



    def comer(self, alimento):
        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True


