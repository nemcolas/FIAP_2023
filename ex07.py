"""Solicite dois números diferentes ao usuário (caso os números sejam iguais, o algoritmo
deve solicitar os números novamente) e informe a diferença entre o maior e o menor
número."""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = n1 - n2

while n1 == n2:
    print("Números iguais, digite novamente!")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

print(f"A diferença entre {n1} e {n2} é de: {n3} ")


