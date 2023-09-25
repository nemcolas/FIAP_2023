letra = input("Informe a letra: ")
letra = letra.lower()
match letra:
    case 's':
        print(" Solteiro")
    case 'c':
        print(" Casado")
    case 'v':
        print(" Viúvo")
    case 'd':
        print (" Divorsiado")
    case _:
        print(" Letra Invalida")