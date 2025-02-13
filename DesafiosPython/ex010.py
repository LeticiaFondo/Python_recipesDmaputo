#crie um programa que leia quanto dinheiro tem em uma carteira e mostre quantos dolares ela pode comprar
carteira = float (input('Qunato dinheiro voce tem na carteira? MZN '))
dolar = carteira / 64
print('Com {:.2f}MZN voce pode comprar {:.2f}USD dolares'.format(carteira, dolar))