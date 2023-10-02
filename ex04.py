cont = 1
dentro = 0
while cont <= 10:
    numero = int(input("informe um número: "))
    if 100 <= numero <= 200:
        dentro += 1
    cont += 1
print (f"{dentro} estão dentro de 100 e 200 ")

