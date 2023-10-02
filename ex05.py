cont = 1
soma_impar = 0
while cont <= 15:
    numero = int(input("Digite o número: "))
    if numero % 3 == 0 or numero == 1:
        soma_impar += numero
    cont += 1
print(f"a soma total dos números ímpares são de: {soma_impar}")
