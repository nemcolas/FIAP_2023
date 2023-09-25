print("1 - Palestra Linux")
print("2 - Palestra de Banco de dados")
print("3 - Palestra de windows server")
print("4 - Palestra sobre Logica de programação")
codigo = int(input("Informe o codigo da palestra: "))
match codigo:
    case 1:
        print("Palestra Linux vai começar em breve no Auditorio 1")
    case 2:
        print ("Palestra Banco de dados vai começar em breve no Auditorio 2")
    case 3:
        print("Palestra de Windows Server vai começar em breve no auditorio 3")
    case 4:
        print("Palestra de Lógica de programação vai começar em breve no auditorio principal")
    case _:
        print("Código Invalido")