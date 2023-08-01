"""
Fazer um programa que pergunte um valor em Dólares e converta para Reais.
Considere que um dólar vale 4,78 reais.
"""

num = float(input("informe um valor monetário em dólares, para ser convertido para o Real (brl):"))

real = num * 4.78

print("O valor inserido convertido em reais é: {:.2f} reais".format(real))