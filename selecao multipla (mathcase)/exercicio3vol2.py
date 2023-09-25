numero = int(input("Informe um número inteiro: "))

resto = numero % 3

match resto:
    case 0:
        print("É Multiplo de 3")
    case _:
        print("Não é multiplo")