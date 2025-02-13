#faca um algoritmo que leia o preco de um produto e mostra seu novo preco com 5% de desconto
preco = float(input('Qual e o preco do produto? MZN'))
disconto = preco - (preco * 5 / 100)
print('O produto que custava {:.2f}MZN, na promocao ira custar {:.2f}MZN.'.format(preco, disconto))