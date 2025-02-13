def verifica_triangulo(a, b, c):
    if (a < b + c) and (b < a + c) and (c < a + b):
        if a == b == c:
            return "Triângulo equilátero"  # Três lados iguais
        elif a == b or a == c or b == c:
            return "Triângulo isósceles"  # Dois lados iguais
        else:
            return "Triângulo escaleno"  # Todos os lados diferentes
    else:
        return "Não é um triângulo"  # Não satisfaz a propriedade

# Exemplos de teste
print(verifica_triangulo(3, 3, 3))  # Triângulo equilátero
print(verifica_triangulo(5, 5, 3))  # Triângulo isósceles
print(verifica_triangulo(4, 5, 6))  # Triângulo escaleno
print(verifica_triangulo(10, 2, 3))  # Não é um triângulo
