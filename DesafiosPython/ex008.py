#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

m = float (input('Digite os metros: '))
c = m * 100
mm = m * 1000
print('{}M equivale a {}CM e {}MM'.format(m, c, mm))
