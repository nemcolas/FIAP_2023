numero = int(input("Informe o número: "))
match numero:
    case _:
        if numero %3 == 0:
            print("É Multiplo de 3")
        else: print("Não é multiplo de 3")