nome = (input("digite o nome do colaborador: "))
carros_vendidos = int(input(f"Informe quantos carros o {nome} vendeu: "))
valor_total_vendas = float(input(f"Informe quanto esses {carros_vendidos} carros somaram no total: "))
comissao_vendas = carros_vendidos * 200
comissao_porcentagem = valor_total_vendas * 0.02
salario_total = 2500 + comissao_vendas + comissao_porcentagem


(print(f"O colaborador {nome} vendeu {carros_vendidos} carros,totalizando {valor_total_vendas: } em vendas, com isso, sua comissão foi de {comissao_vendas + comissao_porcentagem}, Totalizando um salario total de {salario_total}"))


