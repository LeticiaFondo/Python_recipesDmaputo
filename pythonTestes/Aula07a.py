nome = input('Qual e o seu nome?')
print ('Prazer em te conhecer {:20}!'.format(nome))
#print ('Prazer em te conhecer {:<20}!'.format(nome))
#print ('Prazer em te conhecer {:=20}!'.format(nome))
#print ('Prazer em te conhecer {}!'.format(nome))

num1 = int (input('digite um valor: '))
num2 = int (input('digite outro valor: '))
soma  = num1 + num2
divisao = num1 / num2
multiplicacao = num1 * num2
divisaoInteira = num1 // num2
exponenciacao = num1 ** num2

print ('A soma e {},\n o produto e {} e a divisao e {:3f}'.format(soma, divisao, multiplicacao), end = ' ')#o end para deixar tudo na mesma linha
print ('Divisao inteira e {} e a exponenciacao {}!'.format(divisaoInteira, exponenciacao)) # \n e para quebrar a linha
#print ('a soma vale {}'.format(num1+num2))
#soma = num1 + num2
