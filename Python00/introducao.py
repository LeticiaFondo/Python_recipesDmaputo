#comentarios
#variaveis
nome = "Leticia"
idade = 19
peso = 52.15

print(nome)
print(idade)
print(peso)

#operadores
num1 = 10
num2 = 20

soma = num1 + num2
print(soma)
divisao = num1/num2
print(divisao)
multiplicacao = num1 * num2
print(multiplicacao)
subtracao = num1-num2
print(subtracao)


nota = 75

if nota >= 90:
    print("Aprovado com Distinção")
elif nota >= 70:
    print("Aprovado")
else:
    print("Reprovado")



num = 0
while num <= 3:
    print('valor impresso', num)
    num +=1


#match case

print("1. estudante\n"
      "2. trabalhador")


num = int (input("Digite a opcao"))

match num:
    case 1:
        print("Leticia")

    case 2:
        print("Elisio")

    case _:
        print("Opcao invalida")