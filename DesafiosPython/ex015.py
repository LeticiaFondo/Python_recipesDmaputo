dias = int(input('Por quantos dias voce alugou o carro? '))
km = float(input('Por quantos KM voce percorreu com o carro? '))
total = 60 * dias + 0.15 * km


print('O total a pagar e de {}MZN.'.format(total))