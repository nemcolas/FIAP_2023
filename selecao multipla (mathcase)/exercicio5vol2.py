print ("Menu do dia: ")
print (" 1- Picanha")
print("2 - Lasanha")
print("3 - Strogonoff")
print("4 - Bife Acebolado")
print("5 - Pão com ovo")

prato = (int(input("escolha o prato" )))

match prato:
    case 1:
        valor = 25.00
    case 2 | 3:
        valor = 20
    case 4:
        valor = 15
    case 5:
        valor = 5

gorjeta = input("aceita pagar os 10% do garçom? (sim/nao)" ).lower()

match gorjeta:
    case 'sim':
        valor = valor + valor * 0.10
        print(f"valot total R$:{valor}")
    case 'nao':
        print(f"valor total R$:{valor}")

