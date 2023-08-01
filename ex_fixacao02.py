"""
Fazer um programa que pergunte o valor da conta a ser paga no
restaurante. O programa deve apresentar como resposta o valor
da conta com o acrésciomo de 10 % do garçom
"""
num = float(input("Informe o valor da conta à ser pago:"))

acrescimo = num * 10 /100
conta = num + acrescimo

print("O valor total da conta, mais o acréscimo de 10% é {:.2f} reais".format(conta))