#crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada
numero = int (input('Digite um numero: '))
'''''
uma forma de fazer este exercicio
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print('O dobro de {} vale {}!'.format(numero ,dobro))
print('O triplo de {} vale {}!'.format(numero, triplo))
print('A raiz quadrada de {} vale {:.2f}'.format(numero,  raiz))
'''
#outra forma de fazer o mesmo exercicio
print('O dobro de {} vale {}!'.format(numero, (numero*2)))
print('O triplo de {} vale {}!'.format(numero, (numero*3)))
print('A raiz quadrada de {} vale {:.2f}!'.format(numero, (numero**(1/2))))