"""Solicite vários números ao usuário (até que ele digite o número zero) e informe o
somatório dos números digitados.
"""
numero = 1
soma = 0
while numero != 0:
    numero = (int(input("Informe o número: ")))
    soma += numero

print(soma)
