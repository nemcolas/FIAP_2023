cont = 1
menor = 0

while cont <=15:
    idade = int(input("Informe a idade: "))
    if idade < 18:
        menor += 1
    cont += 1
print(f"{menor} são menores de idade")



