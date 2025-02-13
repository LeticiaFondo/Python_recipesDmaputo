#faca um algoritmo que leia o salario de um funcionario e mostre o seu novo salario com o aumento de 15%
salario = float (input('Qual e o seu salario actual? MZN'))
novoSalario = salario + (salario * 15 / 100)
print('O teu salario de {:.2f}MZN teve o aumento de 15% e de agora em diante passa a ser {:.2f}MZN.'.format(salario, novoSalario))