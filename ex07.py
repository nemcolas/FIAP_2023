"""Solicite dois números diferentes ao usuário (caso os números sejam iguais, o algoritmo
deve solicitar os números novamente) e informe a diferença entre o maior e o menor
número."""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

while n1 == n2:
    print("Números iguas, digite novaente!")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))



