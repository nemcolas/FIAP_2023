numero = int(input("Informe um número: "))
print('1 - Dobro do número: ')
print ('2 - Metade do número: ')
print("3 - 10% do número")
opcao = int(input("Informe a opção desejada: "))
match opcao:
    case 1:
        numero = numero + numero
        print(f"resultado é: {numero}")
    case 2:
        numero = numero * 0.5
        print(f"resultado é {numero}")
    case 3:
        numero = numero * 0.10
        print(f"Resultado é {numero}")
    case _:
        print("Caracter invalido")    

