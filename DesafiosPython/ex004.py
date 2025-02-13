#faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo as informacoes possiveis sobre ele
algo = input('digite algo: ')
print('O tipo primitivo desse algo e: ', type(algo))
print('e numerico?', algo.isnumeric())
print('e alfabetico?', algo.isalpha())
print('esta e minusculos?', algo.islower())
print('tem somente espacos? ', algo.isnumeric())