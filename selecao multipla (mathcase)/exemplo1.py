numero1 = float(input("Primeiro número"))
numero2 = float(input("Segundo número"))
opcao = int(input("Informe a opção desejada"))
print("1 - Soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")


match opcao:
    case 1:
        resultado = numero1 + numero2
        print(f"A soma de {numero1} + {numero2} é {resultado}")
    case 2:
        resultado = numero1 - numero2
        print(f"A subtração de `{numero1} + {numero2} é {resultado}")
    case 3:
        resultado = numero1 * numero2
        print (f"a Multiplicação de {numero1} e {numero2} é {resultado}")
    case 4:
        resultado = numero1 / numero2
        print (f"a divisão de {numero1} e {numero2} é {resultado}")
    case _:
        print("Opção invalida")



