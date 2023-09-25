print ("Menu do dia: ")
print (" 1- Picanha")
print("2 - Lasanha")
print("3 - Strogonoff")
print("4 - Bife Acebolado")
print("5 - Pão com ovo")

codigo = int(input("Informe qual prato você deseja comprar: "))
picanha = 25.00
lasanha = 20.00
strogonoff = 20.00
bife = 15.00
pao_com_ovo = 5.00

match codigo:
    case 1:
        sim_ou_nao = int(input("você aceita pagar a gorjeta do garçom? Digite 1 para Sim ou 2 para Não: "))
        if sim_ou_nao == 2:
            print(f"o valor total então é de {picanha} ")
        elif sim_ou_nao == 1:
            print(f"O valor total então é de {picanha + picanha * 0.10}" ) 
        else: print("Codigo invalido")

    case 2:
        sim_ou_nao = int(input("você aceita pagar a gorjeta do garçom? Digite 1 para Sim ou 2 para Não: "))
        if sim_ou_nao == 2:
            print(f"o valor total então é de {lasanha} ")
        elif sim_ou_nao == 1:
            print(f"O valor total então é de {lasanha + lasanha * 0.10}" ) 
        else: print("Codigo invalido")

    case 3:
        sim_ou_nao = int(input("você aceita pagar a gorjeta do garçom? Digite 1 para Sim ou 2 para Não: "))
        if sim_ou_nao == 2:
            print(f"o valor total então é de {strogonoff} ")
        elif sim_ou_nao == 1:
            print(f"O valor total então é de {strogonoff + strogonoff * 0.10}" ) 
        else: print("Codigo invalido")

    case 4:
        sim_ou_nao = int(input("você aceita pagar a gorjeta do garçom? Digite 1 para Sim ou 2 para Não: "))
        if sim_ou_nao == 2:
            print(f"o valor total então é de {bife} ")
        elif sim_ou_nao == 1:
            print(f"O valor total então é de {bife + bife * 0.10}" ) 
        else: print("Codigo invalido")

    case 5:
        sim_ou_nao = int(input("você aceita pagar a gorjeta do garçom? Digite 1 para Sim ou 2 para Não: "))
        if sim_ou_nao == 2:
            print(f"o valor total então é de {pao_com_ovo} ")
        elif sim_ou_nao == 1:
            print(f"O valor total então é de {pao_com_ovo + pao_com_ovo * 0.10}" ) 
        else: print("Codigo invalido")

    case _:
        print("Opção invalida")

