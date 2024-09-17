# Crie um programa que receba um número do usuário e informe se ele é positivo, negativo ou zero.

número = int(input("Digite um número:"))

if número >= 0:
    print("Positivo")

elif número <= 0:
    print("Negativo")

elif número == 0:
    print("Zero")