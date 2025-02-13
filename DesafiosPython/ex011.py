#faca um programa que leia a largura e a altura de uma parede em metros e calcule a area e a suam quantidade necessaria de tinta para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m2
largura = float (input('Digite a largura da parede: '))
altura = float (input('Digite a altura da parede: '))

area = largura * altura
print('Sua parede tem a dimensao de {}x{} e a sua area e de {}m'.format(largura, altura, area))
tinta = area /2
print('Para pintar a sua parede voce pricisara de {}L de tinta.'.format(tinta))